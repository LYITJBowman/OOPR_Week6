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
        try:
            self._room = ROOM(room)
        except ValueError:
            print("Pick a valid room!")
        try:
            self._module = MODULE(module)
        except ValueError:
            print("Pick a valid module!")

    @property
    def name(self):
        return self._name  # getter

    @name.setter
    def name(self, name):
        self._name = name  # cannot be accessed outside of the class

    @name.getter
    def name(self):
        return self._name

    def display_student_details(self):
        print("Student Name: {}".format(self._name))
        self._room.display_room_details()
        self._module.display_module_details()


