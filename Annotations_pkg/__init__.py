#
# File        : __init__.py  
# Created     : 04/11/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

from Annotations_pkg.student_cls import STUDENT

if __name__ == '__main__':
    #Create a student with valid details
    James = STUDENT("James Bowman", "Computer Lab", "Object Orientated Programming")
    James.display_student_details()
    print("\n")
    #Create a student with invalid details
    Marty = STUDENT("Marty McFly", "Prefabs", "Advanced Time Travel")
    #Marty.display_student_details()
