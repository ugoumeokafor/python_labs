#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #for-loop for list objects
    students_list = ["Fred", "Monica", "Niaz", "Adele"]
    for student in students_list:
        print student
    #for-loop for turple objects
    student_tuple = ("Fred", 22, "Monica", 33.5)
    for student in student_tuple:
        print student

if __name__ == '__main__':
    main()
