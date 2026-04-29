#!/usr/bin/python3
"""import"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    my_items = load_from_json_file(filename)
else:
    my_items = []

my_items.extend(sys.argv[1:])
save_to_json_file(my_items, filename)
