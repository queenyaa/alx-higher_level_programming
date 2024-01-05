#!/bin/bash
# script to send a JSON POST request to a URL with the contents

json_file="$2"

if [ -f "$json_file" ]; then
	curl -sX POST -H "Content-Type: application/json" -d @"$json_file" "$1"
else
	echo "Not a valid JSON file"
fi
