#!/bin/bash
# accepts URL sends request to display size of body of response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
