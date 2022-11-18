#!/bin/bash
#Script that takes in a URL as an argument and sends a GET request to the URL
curl -sG "$1" -H "X-School-User-Id: 98"
