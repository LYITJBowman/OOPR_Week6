  #
# File        : decorators_example2.py  
# Created     : 11/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def decorator_fn(funct):
    def wrapper_fun():
        print("Inside wrapper")
        funct()
    return wrapper_fun

def fn_to_be_wrapped():
    print("This is my function ")

if __name__ == '__main__':
    print("Called from Main")
    fn_to_be_wrapped()
    fn_under_wrap = decorator_fn(fn_to_be_wrapped)
    fn_under_wrap()
    print(fn_under_wrap.__name__)