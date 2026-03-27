#!/usr/bin/python3
for i in range(10):
    for h in range(i + 1, 10):
        if i == 8 and h == 9:
            print("{}{}".format(i, h))
        else:
            print("{}{}".format(i, h), end=", ")
