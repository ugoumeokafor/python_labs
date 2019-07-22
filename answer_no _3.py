#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ufu1
#
# Created:     01/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    import os
    import arcpy
    arcpy.env.workspace = r"N:\Lab2_IO"
    feature_classes = arcpy.ListFeatureClasses() #lists the feature classes in the lab 2 folder
    path = r"N:\Lab2_IO"
    try:    #open a file as read and write
        file = open(path + r"\test.txt", "w")   #this just writes the file
        aList = range(1,5)
        n = 1
        for item in feature_classes:
            aString = "File " +  str(n) + ": " + str( item) + "\n" #\n breaks the line
            file.write(aString)
            n = 1+n
        file = open(path + r"\test.txt", "r")   #this now reads the file again
        data = file.read()
        print data #prints the new data
    except Exception as e:
        print e
    finally:
        file.close() #closes the file
        #print "Script ended"


if __name__ == '__main__':
    main()

#arcpy.env.workspace = r"E:\Python_Spring_2017\Lab2_IO"
#feature_classes = arcpy.ListFeatureClasses()