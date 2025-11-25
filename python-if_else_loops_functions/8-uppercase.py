#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print("{}".format(f"{upper_char}"), end="")
    print()
