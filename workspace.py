
# A script to set workspace and list feature classes
import arcpy
arcpy.env.workspace = "E:\Python\Lab1"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:print fc
