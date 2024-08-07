#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    val_ues = {"email": argv[2]}
    url = argv[1]
    req = requests.post(url, data=val_ues)
    print(req.text)


if __name__ == "__main__":
    main(argv)
