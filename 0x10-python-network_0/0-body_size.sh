#!/bin/bash
# This script gets the size of the response body from a given URL.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
