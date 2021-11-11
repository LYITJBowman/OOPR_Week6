#
# File        : Solution.py  
# Created     : 11/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from log_in_cls import LogIn

if __name__ == '__main__':
    new_password = input("Please enter a password: ")
    login = LogIn(new_password)

    print("\nThank You.")
    login.check_password_size()
