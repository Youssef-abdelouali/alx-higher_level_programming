#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
"""
import requests

def main():
    """
    Function that fetches https://alx-intranet.hbtn.io/status
    and displays the body response with type and content
    """
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))

if __name__ == "__main__":
    main()
