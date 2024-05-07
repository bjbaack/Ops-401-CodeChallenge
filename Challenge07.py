#!/usr/bin/env python3

# Script Name:                  Import fernt
# Author:                       Brad Baack
# Date of latest revision:      05/07/2024
# Purpose:             

from cryptography.fernet import Fernet
import os

def write_key():
    """Generate and write a new cryptographic key to a file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved to 'key.key'.")

def load_key():
    """Load the cryptographic key from the key.key file. Generate if not existing."""
    if not os.path.exists("key.key"):
        print("Key file not found. Generating a new key...")
        write_key()
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    """Encrypt the file at the given path using the provided key."""
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        print("File encrypted successfully!")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(file_path, key):
    """Decrypt the file at the given path using the provided key."""
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        print("File decrypted successfully!")
    except Exception as e:
        print(f"Error decrypting file: {e}")

# New function to recursively encrypt a directory
def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# New function to recursively decrypt a directory
def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

if __name__ == "__main__":
    key = load_key()
    while True:
        print("\n~~~~~ Encrypting and Decrypting MENU ~~~~~")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a directory")  # New menu option
        print("4. Decrypt a directory")  # New menu option
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            encrypt_file(file_path, key)
        elif choice == '2':
            file_path = input("Enter the path of the file to decrypt: ")
            decrypt_file(file_path, key)
        elif choice == '3':  # New option handling
            directory_path = input("Enter the path of the directory to encrypt: ")
            encrypt_directory(directory_path, key)
        elif choice == '4':  # New option handling
            directory_path = input("Enter the path of the directory to decrypt: ")
            decrypt_directory(directory_path, key)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
