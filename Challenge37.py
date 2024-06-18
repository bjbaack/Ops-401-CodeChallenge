#!/usr/bin/env python3

# Script Name:                  Challenge 37
# Author:                       Brad Baack
# Date of latest revision:      06/18/2024
# Purpose:                      Cookies 


import requests
import webbrowser
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive an HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
html_content = response_with_cookie.text
html_file_path = "response.html"
with open(html_file_path, "w") as file:
    file.write(html_content)

# Open the .html file with the default web browser
webbrowser.open("file://" + os.path.realpath(html_file_path))

# Stretch Goal
# Give Cookie Monster hands (ASCII art update)
def bringforthcookiemonster_with_hands():
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ''''      )     (     '''''   .'
            ':::. ':  ::' .:::
             ':::.     .:::
               '::.  .::'
                 '::' 
        ''')

bringforthcookiemonster_with_hands()

# Resource
# How To Get / Set HTTP Headers, Cookies And Manage Sessions Using Python Requests Module
# https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/
