#!/usr/bin/python3
"""
Module using request that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    url = "https://intranet.hbtn.io/status"
    re = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(re.text)))
    print("\t- content: {}".format(re.text))


if __name__ == "__main__":
    main()
