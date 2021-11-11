#
# File        : log_in_cls.py  
# Created     : 11/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

class LogIn:
    def __init__(self, password):
        self._password = password

    def check_password_size(self):
        password_len = len(self._password)
        print("The length of your password is {}".format(password_len))

    def password_encrypt(self):
        pass

    def password_compare(self):
        pass
