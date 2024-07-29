#!/usr/bin/python3
"""
Fetches the status of a URL using urllib and prints the response details.
"""
import urllib.request

def fetch_status():
    """
    Fetches and displays the status of a given URL.
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
    
    # Print response details in the specified format
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
