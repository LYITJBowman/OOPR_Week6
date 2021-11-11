#
# File        : wrap_example.py  
# Created     : 11/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from functools import wraps


def decorator_fn(funct):
    @wraps(funct)
    def wrapper_fn():
        print("Inside wrapper")
        funct()
    return wrapper_fn


@decorator_fn
def fn_to_be_wrapped():
    print("This is my function")


if __name__ == '__main__':
    print("Called from Main")
    fn_to_be_wrapped
    print(fn_to_be_wrapped.__name__)

