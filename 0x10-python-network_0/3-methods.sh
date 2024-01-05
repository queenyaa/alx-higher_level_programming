#!/bin/bash
# script to take URL and display all HTTP mthods
curl -sI "$1" | grep -i Allow | awk '{print $2}'
