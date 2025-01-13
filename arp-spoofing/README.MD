# ARP Spoofing Script

This Python script performs ARP spoofing (also known as ARP poisoning) to intercept network traffic between a target machine and a router or another networked device. It sends fake ARP responses to trick the target into thinking the attacker's machine is the destination IP (spoofed IP).

The script is written using the `scapy` library and is intended for educational purposes only. **Use responsibly and only on networks where you have explicit permission to perform penetration testing.**

## Features

- **ARP Spoofing**: Sends crafted ARP packets to the target, claiming the attacker's machine is the gateway or another device on the network.
- **ARP Table Restoration**: Automatically restores the target's ARP table to its original state after the attack is stopped.
- **Continuous Spoofing**: Continually sends ARP spoofing packets every 2 seconds until interrupted by the user.

## Prerequisites

- Python 3.x
- `scapy` library

Install the required library with:

```bash
pip install scapy
```

## Usage

1. Clone or download the script.
2. Run the script from the command line, passing the target IP and the IP to spoof as arguments:

```bash
python arp_spoof.py <target_ip> <spoof_ip>
```

- `<target_ip>`: The IP address of the target device to be spoofed.
- `<spoof_ip>`: The IP address you want to spoof (usually the gateway or router’s IP).

For example:

```bash
python arp_spoof.py 192.168.1.5 192.168.1.1
```

This command will spoof the IP `192.168.1.1` to the target `192.168.1.5`.

## How it Works

1. **Get MAC Address**: The script sends an ARP request to the target IP to retrieve its MAC address.
2. **ARP Spoofing**: It sends spoofed ARP packets to the target, claiming that the spoofed IP is associated with the attacker's MAC address.
3. **ARP Table Restoration**: When the script is interrupted (via `Ctrl+C`), it sends legitimate ARP responses to restore the target's ARP table to its original state.

## Example Output

```bash
[*] Starting ARP spoofing. Press Ctrl+C to stop.
[+] Using attacker MAC address: 00:11:22:33:44:55
[+] Sent fake ARP packet to target 00:11:22:33:44:66: 192.168.1.1 is at 00:11:22:33:44:55
[+] Sent fake ARP packet to target 00:11:22:33:44:66: 192.168.1.1 is at 00:11:22:33:44:55
...
[!] Detected Ctrl+C. Restoring ARP table...
[+] Restored ARP table: 192.168.1.1 -> 00:11:22:33:44:66
[+] ARP table restored. Exiting.
```

## Important Notes

- **Legality**: Ensure you have explicit permission to test the network. Unauthorized ARP spoofing is illegal and unethical.
- **Safety**: It is recommended to use this script in a controlled environment, such as a lab setup or during authorized penetration testing with written consent.

## Disclaimer

This script is intended for educational purposes only. The author does not take responsibility for any misuse or illegal activities. Always act responsibly and within the boundaries of the law.
