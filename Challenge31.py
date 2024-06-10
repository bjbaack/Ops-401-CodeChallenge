#!/usr/bin/env python3

# Script Name:                  Search by file name
# Author:                       Brad Baack
# Date of latest revision:      06/10/2024
# Purpose:                      Search directory on Ubuntu and Windows

import os
import platform
import logging

def search_files(filename, search_directory):
    hits = []
    total_files = 0
    
    # Check the operating system
    if platform.system() == "Windows":
        command = f'dir /s /b "{search_directory}\\{filename}"'
    else:
        command = f'find "{search_directory}" -name "{filename}"'
    
    try:
        # Execute the command and gather results
        result = os.popen(command).read().strip().split('\n')
        for line in result:
            if line:
                hits.append(line)
            total_files += 1
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return hits, total_files

def main():
    # Set up logging
    logging.basicConfig(filename='file_search.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Prompt the user for a file name and directory
    filename = input("Enter the file name to search for: ")
    search_directory = input("Enter the directory to search in: ")

    logging.info(f"Searching for '{filename}' in directory '{search_directory}'")
    
    # Search files
    hits, total_files = search_files(filename, search_directory)
    
    # Display results
    for hit in hits:
        print(f"Found: {hit}")
    
    print(f"\nTotal files searched: {total_files}")
    print(f"Total hits found: {len(hits)}")
    
    logging.info(f"Total files searched: {total_files}")
    logging.info(f"Total hits found: {len(hits)}")

if __name__ == "__main__":
    main()
# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/