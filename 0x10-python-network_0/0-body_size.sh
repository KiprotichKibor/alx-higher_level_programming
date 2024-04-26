#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
response=$(curl -s "$1" -w "%{size_download}") ; echo "$response"
