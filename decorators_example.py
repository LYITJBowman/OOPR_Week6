#
# File        : decorators_example.py  
# Created     : 11/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def outer_function(part_needed, lnumber="L0012345"):
    '''
    :param part_needed:
    :param lnumber:
    :return:
    '''
    print("Lnum in outer is {}".format(lnumber))

    def inner_fn1(lnum=lnumber):
        '''
        :param lnum:
        :return:
        '''
        return lnum[3:]

    def inner_prefix(lnum=lnumber):
        '''
        :param lnum:
        :return:
        '''
        return lnum[0:3]

    if part_needed == "prefix":
        return inner_prefix
    else:
        return inner_fn1

def can_take_fn_as_arg(outer_function):
    '''
    :param outer_function:
    :return:
    '''
    print("Message on outer level is fully visible")
    print("Any function can take another as input")
    outer_function("prefix")

if __name__ == '__main__':
    res = outer_function(part_needed="prefix",lnumber="L0034871847")
    print(res())

    print("\nExample 2")
    can_take_fn_as_arg(outer_function(part_needed="prefix"))
