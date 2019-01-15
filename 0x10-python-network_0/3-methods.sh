#!/bin/bash
# takes a URL and displays all HTTP methods accepted by it
curl -sI $1 | grep 'Allow:' | cut -f2- -d " "
