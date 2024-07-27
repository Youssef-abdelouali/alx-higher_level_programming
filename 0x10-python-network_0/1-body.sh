#!/bin/bash
# Sends a GET request to the URL and displays only the body of the response for a 200 status code
curl -s "$1" -o /tmp/response.txt
grep -q "200" <(curl -s -o /dev/null -w "%{http_code}" "$1") && cat /tmp/response.txt
