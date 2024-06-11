#!/usr/bin/env python3

# Script Name:                  Search by file name
# Author:                       Brad Baack
# Date of latest revision:      06/11/2024 # MOD
# Purpose:                      Search directory on Ubuntu and Windows

import os
import platform
import logging
import hashlib  # MOD
import time  # MOD

def hash_file(filename):  # MOD
    """Generate MD5 hash of the file."""  # MOD
    h = hashlib.md5()  # MOD
    with open(filename, 'rb') as file:  # MOD
        chunk = 0  # MOD
        while chunk != b'':  # MOD
            chunk = file.read(1024)  # MOD
            h.update(chunk)  # MOD
    return h.hexdigest()  # MOD

def search_files(directory):  # MOD
    hits = []  # MOD
    total_files = 0  # MOD
    
    for root, dirs, files in os.walk(directory):  # MOD
        for file in files:  # MOD
            file_path = os.path.join(root, file)  # MOD
            file_hash = hash_file(file_path)  # MOD
            file_size = os.path.getsize(file_path)  # MOD
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # MOD
            print(f"{timestamp} | Hash: {file_hash} | File: {file} | Size: {file_size} bytes | Path: {file_path}")  # MOD
            hits.append(file_path)  # MOD
            total_files += 1  # MOD
    
    return hits, total_files  # MOD

def main():
    # Set up logging
    logging.basicConfig(filename='file_search.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Prompt the user for a directory # MOD
    search_directory = input("Enter the directory to search in: ")  # MOD

    logging.info(f"Searching in directory '{search_directory}'")  # MOD
    
    # Search files # MOD
    hits, total_files = search_files(search_directory)  # MOD
    
    # Display results
    for hit in hits:
        print(f"Found: {hit}")
    
    print(f"\nTotal files searched: {total_files}")  # MOD
    print(f"Total hits found: {len(hits)}")
    
    logging.info(f"Total files searched: {total_files}")
    logging.info(f"Total hits found: {len(hits)}")

if __name__ == "__main__":
    main()

# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://docs.python.org/3/library/hashlib.html # MOD
# https://www.programiz.com/python-programming/examples/hash-file # MOD
