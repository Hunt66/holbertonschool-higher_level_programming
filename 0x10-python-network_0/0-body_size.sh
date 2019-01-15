#!/bin/bash
# accepts URL sends request to display size of body of response
#if [ $1 ]; then
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
#else
#    echo "requires input"
#fi
