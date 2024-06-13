#!/usr/bin/env python3

# Script Name:                  Search by file name
# Author:                       Brad Baack
# Date of latest revision:      06/13/2024
# Purpose:                      Search directory on Ubuntu and Windows

import os
import platform
import logging
import hashlib
import time
import requests

# Hard-code your VirusTotal API key here for initial testing
API_KEY_VIRUSTOTAL = "65ad0b914436ba7a2f05c8cb7621837c903e19b95a21a33265dfddda8453f339"

def hash_file(filename):
    """Generate MD5 hash of the file."""
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def query_virustotal(api_key, file_hash):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {
        'x-apikey': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def search_files(directory):
    hits = []
    total_files = 0
    positives = 0  # MOD
    total_scans = 0  # MOD
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            file_size = os.path.getsize(file_path)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f"{timestamp} | Hash: {file_hash} | File: {file} | Size: {file_size} bytes | Path: {file_path}")
            hits.append(file_path)
            total_files += 1

            # Query VirusTotal
            result = query_virustotal(API_KEY_VIRUSTOTAL, file_hash)
            if result:
                positives += result['data']['attributes']['last_analysis_stats']['malicious']
                total_scans += result['data']['attributes']['last_analysis_stats']['total']

    return hits, total_files, positives, total_scans  # MOD

def main():
    # Set up logging
    logging.basicConfig(filename='file_search.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Prompt the user for a directory
    search_directory = input("Enter the directory to search in: ")

    logging.info(f"Searching in directory '{search_directory}'")
    
    # Search files
    hits, total_files, positives, total_scans = search_files(search_directory)
    
    # Display results
    for hit in hits:
        print(f"Found: {hit}")
    
    print(f"\nTotal files searched: {total_files}")
    print(f"Total hits found: {len(hits)}")
    print(f"VirusTotal scan results: {positives} positives out of {total_scans} scans.")  # MOD
    
    logging.info(f"Total files searched: {total_files}")
    logging.info(f"Total hits found: {len(hits)}")

if __name__ == "__main__":
    main()

# Resources:
# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://docs.python.org/3/library/hashlib.html
# https://www.programiz.com/python-programming/examples/hash-file
# https://docs.virustotal.com/reference/overview#file-scan

