#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
import sys
args = sys.argv[1:]
try:
    stuff = load_from_json_file("add_item.json")
    stuff = stuff + args
    save_to_json_file(stuff, "add_item.json")
except:
    save_to_json_file(args, "add_item.json")
