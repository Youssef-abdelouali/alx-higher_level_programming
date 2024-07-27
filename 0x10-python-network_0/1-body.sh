#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
response=$(curl -s -w "%{http_code}" -o temp_response.txt "$1")
if [ "${response: -3}" -eq 200 ]; then cat temp_response.txt; fi
