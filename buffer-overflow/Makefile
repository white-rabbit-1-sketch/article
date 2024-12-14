CC = gcc
CFLAGS = -O0 -g -fno-inline -fno-builtin -fno-omit-frame-pointer -fno-stack-protector -Wl,--no-omagic,-z,norelro

BUILD_DIR = ./build
SRC_DIR = ./src

default: main

main: main.o
	$(CC) $(CFLAGS) -o $(BUILD_DIR)/main$(EXTENSION) $(BUILD_DIR)/main.o
	as -o $(BUILD_DIR)/shellcode.o $(SRC_DIR)/shellcode.s -g
	ld -o $(BUILD_DIR)/shellcode $(BUILD_DIR)/shellcode.o -g

main.o: $(SRC_DIR)/main.c
	$(CC) $(CFLAGS) -c $(SRC_DIR)/main.c -o $(BUILD_DIR)/main.o

clean:
	$(RM) $(BUILD_DIR)/*