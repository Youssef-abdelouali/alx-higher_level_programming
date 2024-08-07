#!/usr/bin/python3
"""
A script to retrieve the content from https://intranet.hbtn.io/status
"""
import urllib.request

def main():
    """
    Function to display the response from a specified URL.
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Response Body:')
        print('\t- Type: {}'.format(type(html)))
        print('\t- Content: {}'.format(html))
        print('\t- UTF-8 Content: {}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()
