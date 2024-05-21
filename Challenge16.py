#!/usr/bin/env python3

# Script Name:                  Brute Force pt 1
# Author:                       Brad Baack
# Date of latest revision:      05/21/2024
# Purpose:                      Create a brute force attack.

# Import libraries
import time
import getpass
import os

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"  # test filepath
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' # test filepath

    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return
    
    file = open(filepath, encoding="ISO-8859-1")  # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ")
    usr_filepath = input("Let's check the strength of that password.\nPlease enter a dictionary filepath:\n") or "rockyou.txt"  # test filepath
    #usr_filepath = '/home/osboxes/Desktop/rockyou2.txt' # test filepath

    if not os.path.isfile(usr_filepath):
        print(f"File not found: {usr_filepath}")
        return
    
    print(f"Checking password against the words in '{usr_filepath}', just a moment.")
    t1 = time.time()
    file = open(usr_filepath, encoding="ISO-8859-1")  # address encoding problem
    line = file.readline()
    wordlist = []
    while line:
        line = line.rstrip()
        word = line
        wordlist.append(word)
        line = file.readline()
    file.close()
    
    if usr_password not in wordlist:
        print("Your password is acceptable. Good job.")
    else:
        print("Your password was found in the dictionary. Please choose another password.")
    t2 = time.time()
    print(f"Password check completed in {t2 - t1:.2f} seconds.")

# Main
if __name__ == "__main__":  # This condition ensures the script runs only if it is executed directly
    while True:
        print("\nBrute Force Wordlist Attack Tool Menu")
        print("1 - Offensive, Dictionary Iterator")
        print("2 - Defensive, Password Recognized")
        print("3 - Exit")
        
        mode = input("Please enter a number: ")
        
        if mode == "1":
            iterator()  # Call the iterator function if user selects mode 1
        elif mode == "2":
            check_password()  # Call the check_password function if user selects mode 2
        elif mode == "3":
            break  # Exit the loop and end the program if user selects mode 3
        else:
            print("Invalid selection...")  # Print a message if the user enters an invalid selection

# Resources
# https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
