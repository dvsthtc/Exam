import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
env.workspace = r"C:/Users/Anna/Desktop/3d year/programming/exam/Paper_5/4"
inDem = "C:/Users/Anna/Desktop/3d year/programming/exam/Paper_5/4/Elevation"
r = arcpy.GetParameterAsText(0)
x = arcpy.GetParameterAsText(1)
y = arcpy.GetParameterAsText(2)
point = arcpy.Point(x,y)

#arcpy.GetCellValue_management(in_raster, location_point)

#arcpy.Buffer_analysis(point, out_feature_class, r)
