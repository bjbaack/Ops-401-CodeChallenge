#!/usr/bin/env python3

# Script Name:                  Import Scapy
# Author:                       Brad Baack
# Date of latest revision:      05/15/2024
# Purpose:                      Import Scapy and scan ports.

import os  # Used to check for root privileges
import sys  # Used to exit the script if not run as root
from scapy.all import sr1, IP, TCP, ICMP, sr, RandShort  # Scapy components for network packet creation and handling
import ipaddress  # Used to validate network addresses and CIDR notation

# Check for root privileges
if os.geteuid() != 0:
    print("This script must be run as root!")
    sys.exit(1)

# Function to scan TCP ports on a target host
def tcp_port_scanner(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        # Create a SYN packet for the current port with a random source port
        packet = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='S')
        # Send the packet and wait for a response
        response = sr1(packet, timeout=1, verbose=0)

        if response:  # If a response is received
            if response.haslayer(TCP):  # Check if the response has a TCP layer
                tcp_layer = response.getlayer(TCP)
                if tcp_layer.flags == 0x12:  # SYN-ACK response (port is open)
                    print(f"Port {port} is open.")
                    # Send a RST packet to close the connection
                    rst_pkt = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='R')
                    sr1(rst_pkt, timeout=1, verbose=0)
                elif tcp_layer.flags == 0x14:  # RST-ACK response (port is closed)
                    print(f"Port {port} is closed.")
            else:
                # If the response does not have a TCP layer, it is filtered
                print(f"Port {port} is filtered.")
        else:
            # If no response is received, the port is filtered
            print(f"Port {port} is filtered.")

# Function for ICMP Ping Sweep to check live hosts in a network
def icmp_ping_sweep(network):
    net = ipaddress.ip_network(network, strict=False)  # Define the network
    live_hosts = 0  # Counter for live hosts

    for ip in net.hosts():
        # Create an ICMP echo request packet
        packet = IP(dst=str(ip)) / ICMP()
        # Send the packet and wait for a response
        response = sr1(packet, timeout=1, verbose=0)

        if response:  # If a response is received
            if response.haslayer(ICMP):  # Check if the response has an ICMP layer
                icmp_layer = response.getlayer(ICMP)
                if icmp_layer.type == 0:  # Echo Reply
                    print(f"{ip} is responding.")
                    live_hosts += 1
                elif icmp_layer.type == 3 and icmp_layer.code in [1, 2, 3, 9, 10, 13]:
                    # Host is actively blocking ICMP traffic
                    print(f"{ip} is actively blocking ICMP traffic.")
                else:
                    # Host is unresponsive to ICMP ping
                    print(f"{ip} is unresponsive.")
        else:
            # Host is down or unresponsive to ICMP ping
            print(f"{ip} is down or unresponsive.")

    # Print the total number of live hosts found
    print(f"Total live hosts: {live_hosts}")

# Function to perform an ICMP ping to check if the host is responsive
def icmp_ping(host):
    # Create an ICMP echo request packet
    packet = IP(dst=host) / ICMP()
    # Send the packet and wait for a response
    response = sr1(packet, timeout=1, verbose=0)

    if response:  # If a response is received
        if response.haslayer(ICMP):  # Check if the response has an ICMP layer
            icmp_layer = response.getlayer(ICMP)
            if icmp_layer.type == 0:  # Echo Reply
                print(f"{host} is responding.")
                return True
            elif icmp_layer.type == 3 and icmp_layer.code in [1, 2, 3, 9, 10, 13]:
                # Host is actively blocking ICMP traffic
                print(f"{host} is actively blocking ICMP traffic.")
            else:
                # Host is unresponsive to ICMP ping
                print(f"{host} is unresponsive.")
        else:
            # Host is unresponsive to ICMP ping
            print(f"{host} is unresponsive.")
    else:
        # Host is down or unresponsive to ICMP ping
        print(f"{host} is down or unresponsive.")
    return False

# Main section of the script
if __name__ == "__main__":
    while True:
        # Prompt the user to select a mode
        print("Select Mode:")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        mode = input("Enter choice: ")

        if mode == '1':
            # If mode 1 is selected, prompt for IP address and port range
            host_ip = input("Enter the IP address to scan: ")
            try:
                start_port = int(input("Enter the start port: "))
                end_port = int(input("Enter the end port: "))
                # Perform a TCP port scan on the specified IP address and port range
                tcp_port_scanner(host_ip, start_port, end_port)
            except ValueError:
                # Handle invalid port number input
                print("Invalid port number. Please enter numeric values.")
        elif mode == '2':
            # If mode 2 is selected, prompt for network address with CIDR block
            network = input("Enter the network address with CIDR block (e.g., 192.168.1.0/24): ")
            try:
                # Validate the network address
                ipaddress.ip_network(network, strict=False)
                # Perform an ICMP ping sweep on the specified network
                icmp_ping_sweep(network)
            except ValueError:
                # Handle invalid network address input
                print("Invalid network address. Please enter a valid CIDR notation.")
        else:
            # Handle invalid mode selection
            print("Invalid choice. Please select 1 or 2.")
