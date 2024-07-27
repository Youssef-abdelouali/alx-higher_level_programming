#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument with the content of a file passed as the second argument.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
