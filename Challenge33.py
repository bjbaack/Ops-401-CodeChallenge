import os
import hashlib
import requests
from virustotal_search import VirusTotalAPI  # Assuming virustotal_search.py has a class named VirusTotalAPI

def get_api_key():
    return os.getenv('API_KEY_VIRUSTOTAL')

def hash_file(file_path):
    """Generate MD5 hash of the file."""
    h = hashlib.md5()
    with open(file_path, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def query_virustotal(api_key, file_hash):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {
        'x-apikey': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = get_api_key()
    if not api_key:
        print("API key for VirusTotal not set. Please set it as an environment variable.")
        return
    
    file_path = input("Enter the path of the file to scan: ")
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return
    
    file_hash = hash_file(file_path)
    print(f"MD5 hash of the file: {file_hash}")
    
    # Using virustotal_search.py functionality if necessary
    vt = VirusTotalAPI(api_key)
    result = vt.file_report(file_hash)
    
    if result:
        positives = result['data']['attributes']['last_analysis_stats']['malicious']
        total = result['data']['attributes']['last_analysis_stats']['total']
        print(f"VirusTotal scan results: {positives} positives out of {total} scans.")
    else:
        print("Failed to retrieve data from VirusTotal.")
    
if __name__ == "__main__":
    main()
