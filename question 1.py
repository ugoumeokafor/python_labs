#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ufu1
#
# Created:     08/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import os
    import arcpy
    arcpy.env.workspace = r"N:\Lab2_IO"
    fc = "Census_Tracts.shp"

    if arcpy.Exists(fc): #The Exists function honors the geoprocessing workspace environment allowing you to just specify the base name (fc), in this case it checks if the feature class Census Tracts exists in the folder.
        print "I did find Census_Tracts.shp feature in that folder"
    else:
        print "I didn't find it"


if __name__ == '__main__':
    main()
