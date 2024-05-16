#!/usr/bin/env python3

# Script Name:                  Import Scapy
# Author:                       Brad Baack
# Date of latest revision:      05/15/2024
# Purpose:                      Import Scapy and scan ports.

from scapy.all import sr1, IP, ICMP, TCP

def ping_host(ip):
    # Send an ICMP packet to the target IP address and wait for a response
    response = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=0)
    # Return True if there is a response, indicating the host is reachable
    return response is not None

def scan_ports(ip):
    # Define a list of common ports to scan
    common_ports = [22, 23, 443]
    # List to store open ports
    open_ports = []

    for port in common_ports:
        # Send a TCP SYN packet to the target IP and port
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
        # Check if the response is a TCP SYN-ACK packet, indicating the port is open
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            # Add the open port to the list
            open_ports.append(port)
            # Send a TCP RST packet to close the connection
            sr1(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
    
    # Print the list of open ports or a message if no ports are open
    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip}.")

def main():
    while True:
        # Prompt the user to enter an IP address or 'exit' to stop
        ip = input("Enter an IP address to scan (or 'exit' to stop): ")
        if ip.lower() == 'exit':
            break
        # Ping the host to check if it's reachable
        if ping_host(ip):
            print(f"Host {ip} is reachable.")
            # Scan the ports if the host is reachable
            scan_ports(ip)
        else:
            print(f"Host {ip} is not reachable.")

if __name__ == "__main__":
    main()
