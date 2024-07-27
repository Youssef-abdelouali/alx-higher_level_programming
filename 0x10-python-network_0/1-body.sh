#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
response=$(curl -s -w "%{http_code}" "$1")
body=$(echo "$response" | head -n1)
status_code=$(echo "$response" | tail -n1)

if [ "$status_code" -eq 200 ]; then
  echo "$body"
fi
