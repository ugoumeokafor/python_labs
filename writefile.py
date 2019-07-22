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
        file = open(path + r"\test.txt", "w")   #this just writes the file
        file.write("something") #write text in the file
        aList = range(1,4)
        for item in aList:
            aString = "\n""Line" + str(item) + "\n" #\n breaks the line
            file.write(aString)
        file = open(path + r"\test.txt", "r")   #this now reads the file again
        data = file.read()
        print data
    except Exception as e:
        print e
    finally:
        file.close()
        print "Script ended"


if __name__ == '__main__':
    main()

#arcpy.env.workspace = r"E:\Python_Spring_2017\Lab2_IO"
#feature_classes = arcpy.ListFeatureClasses()
