#
# File        : student_cls.py  
# Created     : 04/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Student Class
#

"""Student Class File"""
from Annotations_pkg.room_cls import ROOM
from Annotations_pkg.module_cls import MODULE

class STUDENT:
    def __init__(self, name, room, module):
        self._name = name  # cannot be accessed outside of the class
        self._room = ROOM(room)
        self._module = MODULE(module)

    @property
    def name(self):
        return self._name  # getter

    @property
    def room(self):
        return self._room  # getter

    @property
    def module(self):
        return self._module  # getter

    @name.setter
    def name(self, name):
        self._name = name  # cannot be accessed outside of the class

    @room.setter
    def room(self, name):
        self._room = room  # cannot be accessed outside of the class

    @module.setter
    def module(self, module):
        self._module = module  # cannot be accessed outside of the class

    @name.getter
    def name(self):
        return self._name

    @room.getter
    def room(self):
        return self._room

    @module.getter
    def module(self):
        return self._module

    def display_student_details(self):
        print("Student Name: {}".format(self._name))
        print("Room: ()".format(self._room))
        print("Module: ()".format(self._module))


