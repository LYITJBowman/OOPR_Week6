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
    James = STUDENT("James Bowman", "Computer Lab", "Object Orientated Programming")
    James.display_student_details()

    Marty = STUDENT("Marty McFly", "Prefabs", "Advanced Time Travel")
