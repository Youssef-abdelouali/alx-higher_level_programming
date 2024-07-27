#!/bin/bash
<<<<<<< HEAD
# Sends a request to a URL and displays the size of the response body in bytes
curl -s "$1" | wc -c
=======
# This script gets the size of the response body from a given URL.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
>>>>>>> e291a603555a68d957db458d21db0f80d36d3e20
