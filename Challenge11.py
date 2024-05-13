#!/usr/bin/env python3

# Script Name:                  Import Scapy
# Author:                       Brad Baack
# Date of latest revision:      05/13/2024
# Purpose:                      Import Scapy and scan ports. 


from scapy.all import sr1, IP, TCP

def tcp_port_scanner(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        packet = IP(dst=host) / TCP(dport=port, flags='S')
        response = sr1(packet, timeout=1, verbose=0)

        if response:
            if response.haslayer(TCP):
                tcp_layer = response.getlayer(TCP)  # Corrected from TTCP to TCP
                if tcp_layer.flags == 0x12:
                    print(f"Port {port} is open.")
                    rst_pkt = IP(dst=host) / TCP(dport=port, flags='R')
                    sr1(rst_pkt, timeout=1, verbose=0)
                elif tcp_layer.flags == 0x14:
                    print(f"Port {port} is closed.")
            else:
                print(f"Port {port} is filtered.")
        else:
            print(f"Port {port} is filtered.")

if __name__ == "__main__":
    host_ip = "192.168.1.1"  # Replace with the IP address you want to scan
    start_port = 1
    end_port = 100

    tcp_port_scanner(host_ip, start_port, end_port)
