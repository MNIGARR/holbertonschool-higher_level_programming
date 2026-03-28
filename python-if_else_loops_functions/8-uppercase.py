#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            b = chr(ord(a) - 32)
        else:
            b = a
        print("{}".format(b), end="")
    print("")
