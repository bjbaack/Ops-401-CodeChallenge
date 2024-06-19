#!/usr/bin/env python3

# Script Name:                  Challenge 37
# Author:                       Brad Baack
# Date of latest revision:      06/18/2024
# Purpose:                      Cookies 

import requests
from bs4 import BeautifulSoup as bs

# Function to test for XSS vulnerability
def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        print(f"XSS vulnerability found in {url}")
    else:
        print(f"No XSS vulnerability found in {url}")

# URLs to test
urls = [
    "https://xss-game.appspot.com/level1/frame", # Should be positive
    "http://dvwa.local/login.php"               # Should be negative
]

# Test each URL
for url in urls:
    test_xss(url)
