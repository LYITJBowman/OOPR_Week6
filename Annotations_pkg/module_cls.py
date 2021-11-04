#
# File        : module_cls.py  
# Created     : 04/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Module Class
#

"""Module Class File"""

Modules_List = {"Object Orientated Programming", "Software Engineering"}


class MODULE:
    def __init__(self, name):
        self._module_name = name  # cannot be accessed outside of the class

    @property
    def module_name(self):
        return self._module_name  # getter

    @module_name.setter
    def module_name(self, name):
        """Restricting to the available valid module names"""
        if name not in Modules_List:
            raise ValueError("Invalid Module Name")
        self._module_name = name  # cannot be accessed outside of the class

    def display_module_details(self):
        print("Module Name: {}".format(self._module_name))
