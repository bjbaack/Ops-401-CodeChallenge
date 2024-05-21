#!/usr/bin/env python3

# Script Name:                  Brute Force pt 1
# Author:                       Brad Baack
# Date of latest revision:      05/21/2024
# Purpose:                      Create a brute force attack.

# Import libraries
import time  # Import time module for delays
import getpass  # Import getpass module to securely get user passwords
import os  # Import os module for file system operations

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"  # Prompt user for file path, default to 'rockyou.txt'
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' # Alternative test filepath

    if not os.path.isfile(filepath):  # Check if the file exists
        print(f"File not found: {filepath}")  # Print error message if file not found
        return  # Exit the function
    
    file = open(filepath, encoding="ISO-8859-1")  # Open the file with appropriate encoding
    line = file.readline()  # Read the first line from the file
    while line:  # Loop until no more lines in the file
        line = line.rstrip()  # Remove any trailing whitespace from the line
        word = line  # Assign the cleaned line to the variable word
        print(word)  # Print the word
        time.sleep(1)  # Delay for 1 second
        line = file.readline()  # Read the next line from the file
    file.close()  # Close the file

def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ")  # Securely get the user's password
    usr_filepath = input("Let's check the strength of that password.\nPlease enter a dictionary filepath:\n") or "rockyou.txt"  # Prompt user for file path, default to 'rockyou.txt'
    #usr_filepath = '/home/osboxes/Desktop/rockyou2.txt' # Alternative test filepath

    if not os.path.isfile(usr_filepath):  # Check if the file exists
        print(f"File not found: {usr_filepath}")  # Print error message if file not found
        return  # Exit the function
    
    print(f"Checking password against the words in '{usr_filepath}', just a moment.")  # Inform the user about the check
    t1 = time.time()  # Record the start time
    file = open(usr_filepath, encoding="ISO-8859-1")  # Open the file with appropriate encoding
    line = file.readline()  # Read the first line from the file
    wordlist = []  # Initialize an empty list to store words
    while line:  # Loop until no more lines in the file
        line = line.rstrip()  # Remove any trailing whitespace from the line
        word = line  # Assign the cleaned line to the variable word
        wordlist.append(word)  # Append the word to the wordlist
        line = file.readline()  # Read the next line from the file
    file.close()  # Close the file
    
    if usr_password not in wordlist:  # Check if the password is not in the wordlist
        print("Your password is acceptable. Good job.")  # Print message if password is not found
    else:
        print("Your password was found in the dictionary. Please choose another password.")  # Print message if password is found
    t2 = time.time()  # Record the end time
    print(f"Password check completed in {t2 - t1:.2f} seconds.")  # Print the duration of the check

# Main
if __name__ == "__main__":  # This condition ensures the script runs only if it is executed directly
    while True:  # Start an infinite loop
        print("\nBrute Force Wordlist Attack Tool Menu")  # Print the menu
        print("1 - Offensive, Dictionary Iterator")  # Option 1: Run the iterator function
        print("2 - Defensive, Password Recognized")  # Option 2: Run the check_password function
        print("3 - Exit")  # Option 3: Exit the program
        
        mode = input("Please enter a number: ")  # Get user input for menu option
        
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
