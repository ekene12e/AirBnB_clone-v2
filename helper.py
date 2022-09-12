#!/usr/bin/python3
""" Console helper functions"""

def assign_values(obj, args={}):
    for key, val in args.items():
        setattr(obj, key, val)

def break_to_dict(args):
    arg_list = args.split(' ')
    my_dict = {}
    return arg_list

print(break_to_dict('name="hello" u="me" k=4'))
