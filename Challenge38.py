#!/usr/bin/env python3

# Script Name:                  Challenge 37
# Author:                       Brad Baack
# Date of latest revision:      06/18/2024
# Purpose:                      Cookies 

#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: A script to detect XSS vulnerabilities in web forms by injecting a payload and checking the response.
# Date:        TODO: Add date
# Modified by: TODO: Add your name

# Make sure to install requests and bs4 before executing this in Python3
# You can install them using pip:
# pip3 install requests bs4

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Function to get all forms from a URL
# This function fetches the HTML content of the given URL, parses it, and returns all form tags found.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to extract details of a form
# This function takes a form element as input and extracts its action URL, method, and input fields.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form with a given payload
# This function constructs a full URL from the form's action attribute and the base URL, fills the form inputs with a given value (payload), and submits it.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to scan a URL for XSS vulnerabilities
# This function iterates over all forms in the given URL, submits a payload, and checks if the payload is reflected in the response, indicating a potential XSS vulnerability.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"  # Payload to test for XSS vulnerability
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main function to run the script
# This function prompts the user for a URL, then calls the scan_xss function to check for vulnerabilities.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

# TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
# TODO: Test this script against one XSS-positive target and one XSS-negative target
# TODO: Paste the outputs here as comments in this script, clearly indicating which is positive detection and negative detection
