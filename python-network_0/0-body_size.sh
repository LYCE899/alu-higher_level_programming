#!/bin/bash
#Script that takes in a URL, sends a request to the URL
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
