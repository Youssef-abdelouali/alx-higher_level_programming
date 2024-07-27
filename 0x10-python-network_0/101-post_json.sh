#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument and displays the body of the response.
# The content of the JSON file is passed as the second argument in the body of the request.

curl -s -H "Content-Type: application/json" -d @"$2" "$1"
