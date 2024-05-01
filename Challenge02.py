#!/usr/bin/env python3

# Script Name:                  Import Time
# Author:                       Brad Baack
# Date of latest revision:      04/30/2024
# Purpose:                      Ping an IP every 2 seconds



# Import necessary libraries
import time
from datetime import datetime
from ping3 import ping

# Define a function to check the network status of a specific IP address
def check_host(ip):
    try:
        # Transmit a single ICMP (ping) packet to check if host is up
        response = ping(ip)
        # Evaluate the response; no response indicates the network is inactive
        if response is None:
            return 'Network Inactive'
        else:
            # A response indicates the network is active
            return 'Network Active'
    except exceptions.PingError:
        # Handle exceptions that may occur during the ping process
        return 'Ping Error'

# Main function to continuously monitor a specified IP address
def main():
    host_ip = "8.8.8.8"  # Google IP address to monitor
    while True:
        # Check the network status of the IP address
        status = check_host(host_ip)
        # Get the current time for a comprehensive timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # Print the timestamp, network status, and the IP address being tested
        print(f"{timestamp} {status} to {host_ip}")
        # Wait for two seconds before sending the next ping
        time.sleep(2)

# Ensure that the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
