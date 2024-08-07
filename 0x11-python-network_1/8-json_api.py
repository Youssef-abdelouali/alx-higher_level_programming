#!/usr/bin/python3
"""
Module sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


def main():
    """
    Script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        result = response.json()
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result["id"], result["name"]))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
