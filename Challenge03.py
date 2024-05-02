#!/usr/bin/env python3

# Script Name:                  Uptime Sensor Tool
# Author:                       Brad Baack
# Date of latest revision:      05/01/2024
# Purpose:                      

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Function to send email
def send_email(user_email, password, host, previous_status, current_status):
    to_email = "admin@example.com"  # Administrator's email
    subject = f"Status Change Notification for {host}"
    message = f"Host {host} status changed from {previous_status} to {current_status} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = to_email
    msg['Subject'] = subject
    body = MIMEText(message, 'plain')
    msg.attach(body)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, password)
    text = msg.as_string()
    server.sendmail(user_email, to_email, text)
    server.quit()
    
    print("Email sent successfully!")

# Main script logic
def main():
    user_email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    # Example status change, this part would normally be handled by your monitoring logic
    host = "ExampleHost"
    previous_status = "down"
    current_status = "up"
    
    send_email(user_email, password, host, previous_status, current_status)

if __name__ == "__main__":
    main()