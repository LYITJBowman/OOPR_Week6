#
# File        : room_cls.py  
# Created     : 04/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Room Class
#

"""Room Class File"""

Room_List = {"Main Lecture Hall", "Computer Lab"}


class ROOM:
    def __init__(self, name):
        self._room_name = name  # cannot be accessed outside of the class

    @property
    def room_name(self):
        return self._room_name  # getter

    @room_name.setter
    def room_name(self, name):
        """Restricting to the available valid room names"""
        if name not in Room_List:
            raise ValueError("Invalid Room Name")
        self._room_name = name  # cannot be accessed outside of the class

    def display_room_details(self):
        print("Room Name: {}".format(self._room_name))
