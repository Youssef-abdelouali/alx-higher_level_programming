#!/usr/bin/python3
"""
Module to fetch and display commits from a GitHub repository
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth  # Optional, if you need authentication


def fetch_commits(owner, repo):
    """
    Fetch the most recent commits from the specified GitHub repository.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure we raise an exception for HTTP errors
    return response.json()


def display_commits(commits, limit=10):
    """
    Display up to `limit` num of commits, showing their SHA and author names.
    """
    for commit in commits[:limit]:
        sha = commit.get("sha")
        commit_info = commit.get("commit", {})
        author = commit_info.get("author", {})
        name = author.get("name", "Unknown")
        print(f"{sha}: {name}")


def main():
    """
    Main function that handles command-line arguments and prints the commits.
    """
    if len(argv) != 3:
        print("Usage: ./script.py <repository> <owner>")
        return

    repo = argv[1]
    owner = argv[2]
    commits = fetch_commits(owner, repo)
    display_commits(commits)


if __name__ == "__main__":
    main()
