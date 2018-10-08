#!/usr/bin/python3
"""Nqueens puzzle
"""
import sys
args = sys.argv[1:]
argc = len(args)
if argc != 1:
    print("Usage: nqueens N")
    exit(1)
arg = args[0]
if not isinstance(arg, int):
    print("N must be a number")
    exit(1)
if arg < 4:
    print("N must be at least 4")
    exit(1)
