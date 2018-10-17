#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as f:
        st = ''
        for line in (f.readlines()):
            st += line
            if search_string in line:
                st += new_string
        f.seek(0)
        f.write(st)
