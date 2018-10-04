#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            text = text[:i + 1] + '\n\n' + text[i + 2:]
    print(text)
