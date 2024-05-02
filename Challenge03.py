#!/usr/bin/env python3

# Script Name:                  Uptime Sensor Tool
# Author:                       Brad Baack
# Date of latest revision:      05/01/2024
# Purpose:                      


import smtplib
import datetime

# Function to send email
def send_email(user_email, to_email, password, host, previous_status, current_status):
    subject = f"Status Change Notification for {host}"
    message = f"Subject: {subject}\n"
    message += f"Host {host} status changed from {previous_status} to {current_status} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."

    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS encryption
    server.login(user_email, password)  # Log in to your email account
    server.sendmail(user_email, to_email, message)  # Send the email
    server.quit()  # Quit the server

    print("Email sent successfully!")

# Main script logic
def main():
    user_email = input("Enter your email address: ")
    password = input("Enter your password: ")
    to_email = "administrator@example.com"  # Administrator's email

    # Example status change, this part would normally be handled by your monitoring logic
    host = "ExampleHost"
    previous_status = "down"
    current_status = "up"
    
    send_email(user_email, to_email, password, host, previous_status, current_status)

if __name__ == "__main__":
    main()
