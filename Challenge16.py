#!/usr/bin/env python3

# Script Name:                  Brute Force pt 1
# Author:                       Brad Baack
# Date of latest revision:      05/21/2024
# Purpose:                      Create a brute force attack.

# Import libraries
import time

# Declare functions
def iterator():
    # This function iterates over each word in the provided wordlist file and prints it with a delay.
    filepath = input("Enter your dictionary filepath:\n")  # Prompt user for the file path
    try:
        with open(filepath, encoding="ISO-8859-1") as file:  # Open the file with appropriate encoding
            for line in file:  # Read each line in the file
                word = line.strip()  # Strip any leading/trailing whitespace from the line
                print(word)  # Print the current word
                time.sleep(1)  # Add a delay of 1 second
    except FileNotFoundError:
        print(f"File not found: {filepath}")  # Handle the case where the file is not found

def check_password():
    # This function checks if a user-provided string exists in the provided wordlist file.
    user_string = input("Enter the string to search: ")  # Prompt user for the string to search
    filepath = input("Enter your dictionary filepath:\n")  # Prompt user for the file path
    try:
        with open(filepath, encoding="ISO-8859-1") as file:  # Open the file with appropriate encoding
            words = file.read().splitlines()  # Read all lines into a list of words
            if user_string in words:  # Check if the user-provided string is in the list
                print("The word is in the dictionary")  # Print if found
            else:
                print("The word is not in the dictionary")  # Print if not found
    except FileNotFoundError:
        print(f"File not found: {filepath}")  # Handle the case where the file is not found

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


#Resources
# https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
