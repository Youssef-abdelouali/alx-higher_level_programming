#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
Manages HTTPError exceptions and prints the error code.
"""
import urllib.request
import urllib.error
import sys

def main():
    """
    Method that manages urllib.error.HTTPError exceptions and
    prints: Error code: followed by the HTTP status code.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
