#!/usr/bin/python3
"""
Module to access the GitHub API using credentials
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main():
    """
    Script that takes GitHub credentials (username and password) from the CLI,
    makes a request to the GitHub API, and displays the user's GitHub ID.
    """
    if len(argv) != 3:
        print("Usage: ./script.py <username> <password>")
        return

    user = argv[1]
    password = argv[2]
    response = requests.get(
        "https://api.github.com/user", auth=HTTPBasicAuth(user, password)
    )

    try:
        profile_info = response.json()
        print(profile_info.get("id", "None"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    main()
