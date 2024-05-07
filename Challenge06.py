#!/usr/bin/env python3

# Script Name:                  Import fernt
# Author:                       Brad Baack
# Date of latest revision:      05/06/2024
# Purpose:             

from cryptography.fernet import Fernet

def generate_and_save_key():
    # Generates a key and saves it to a file
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    # Loads the key from the 'secret.key' file
    return open("secret.key", "rb").read()

def encrypt_message(message):
    # Encrypts a message
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    # Decrypts a message
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Main execution
if __name__ == "__main__":
    generate_and_save_key()  # Generate and save a new key
    message = "welcome to cybersecurity"
    encrypted = encrypt_message(message)
    print("Ciphertext:", encrypted.decode())
    
    decrypted = decrypt_message(encrypted)
    print("Plaintext:", decrypted)
