import os
import sys
from scapy.all import sr1, IP, TCP, ICMP, sr
import ipaddress

# Check for root privileges
if os.geteuid() != 0:
    print("This script must be run as root!")
    sys.exit(1)

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

# New function for ICMP Ping Sweep
def icmp_ping_sweep(network):
    net = ipaddress.ip_network(network, strict=False)
    live_hosts = 0

    for ip in net.hosts():
        packet = IP(dst=str(ip)) / ICMP()
        response = sr1(packet, timeout=1, verbose=0)

        if response:
            if response.haslayer(ICMP):
                icmp_layer = response.getlayer(ICMP)
                if icmp_layer.type == 0:  # Echo Reply
                    print(f"{ip} is responding.")
                    live_hosts += 1
                elif icmp_layer.type == 3 and icmp_layer.code in [1, 2, 3, 9, 10, 13]:
                    print(f"{ip} is actively blocking ICMP traffic.")
                else:
                    print(f"{ip} is unresponsive.")
        else:
            print(f"{ip} is down or unresponsive.")

    print(f"Total live hosts: {live_hosts}")

if __name__ == "__main__":
    while True:
        print("Select Mode:")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        mode = input("Enter choice: ")

        if mode == '1':
            host_ip = input("Enter the IP address to scan: ")
            try:
                start_port = int(input("Enter the start port: "))
                end_port = int(input("Enter the end port: "))
                tcp_port_scanner(host_ip, start_port, end_port)
            except ValueError:
                print("Invalid port number. Please enter numeric values.")
        elif mode == '2':
            network = input("Enter the network address with CIDR block (e.g., 192.168.1.0/24): ")
            try:
                ipaddress.ip_network(network, strict=False)
                icmp_ping_sweep(network)
            except ValueError:
                print("Invalid network address. Please enter a valid CIDR notation.")
        else:
            print("Invalid choice. Please select 1 or 2.")
