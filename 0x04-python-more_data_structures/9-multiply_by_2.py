#!/usr/bin/python3
def multiply_by_2(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
