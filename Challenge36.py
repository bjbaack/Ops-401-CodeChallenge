
#!/usr/bin/env python3

# Script Name:                  Search by file name
# Author:                       Brad Baack
# Date of latest revision:      06/13/2024
# Purpose:                      Search directory on Ubuntu and Windows

import os
import subprocess

def banner_grab_with_netcat(target, port):
    print(f"\n[+] Banner grabbing using Netcat on {target}:{port}")
    try:
        result = subprocess.check_output(f"nc -vz {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Netcat command timed out.")

def banner_grab_with_telnet(target, port):
    print(f"\n[+] Banner grabbing using Telnet on {target}:{port}")
    try:
        result = subprocess.check_output(f"echo '' | telnet {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Telnet command timed out.")

def banner_grab_with_nmap(target):
    print(f"\n[+] Banner grabbing using Nmap on {target}")
    try:
        result = subprocess.check_output(f"nmap -sV {target}", shell=True, stderr=subprocess.STDOUT, timeout=60)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Nmap command timed out.")

def main():
    target = input("Enter the URL or IP address: ")
    port = input("Enter the port number: ")

    banner_grab_with_netcat(target, port)
    banner_grab_with_telnet(target, port)
    banner_grab_with_nmap(target)

if __name__ == "__main__":
    main()
