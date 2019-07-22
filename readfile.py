#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ufu1
#
# Created:     30/01/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import os
    path = r"E:\Python_Spring_2017\Lab2_IO"
    try:    #open a file as read only
        file = open(path + r"\test.txt", "r")
        data = file.read()
        print data
    except Exception as e:
        print e
    finally:
        file.close()
        print "Script ended"


if __name__ == '__main__':
    main()
