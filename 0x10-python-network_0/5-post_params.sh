#!/bin/bash
# takes URL sends POST request and displays the body response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
