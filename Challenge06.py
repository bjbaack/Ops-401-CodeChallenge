#!/usr/bin/env python3

# Script Name:                  Import fernt
# Author:                       Brad Baack
# Date of latest revision:      05/06/2024
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

def encrypt_message(message, key):
    """Encrypt a plaintext message."""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """Decrypt an encrypted message."""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    key = load_key()
    while True:
        print("\n~~~~~ Encrypting and Decrypting MENU ~~~~~")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            encrypt_file(file_path, key)
        elif choice == '2':
            file_path = input("Enter the path of the file to decrypt: ")
            decrypt_file(file_path, key)
        elif choice == '3':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message.decode()}")
        elif choice == '4':
            encrypted_message = input("Enter the encrypted message to decrypt: ")
            try:
                decrypted_message = decrypt_message(encrypted_message.encode(), key)
                print(f"Decrypted message: {decrypted_message}")
            except Exception as e:
                print(f"Error decrypting message: {e}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
