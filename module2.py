#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(): #for-loop for dictionary objects
    students_dict = {'name': 'Fred', 'age':27, 'major':'GIS'}
    for item in students_dict:
        print item
    #have a look at the difference of output
    for item in students_dict.keys():
        print item
    for item in students_dict.keys():
        print students_dict[item]
    for item in students_dict.values():
        print item
    for i, j in students_dict.iteritems():
        print i+':'+str(j)+','


if __name__ == '__main__':
    main()
