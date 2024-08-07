#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
import sys

def main():
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id', 'Header not found'))

if __name__ == "__main__":
    main()
