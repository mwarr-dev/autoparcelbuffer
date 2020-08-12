# Import system modules
import arcpy

# Set the workspace
arcpy.env.workspace = 'F:\MWARREN\_scratch\_scratch.gdb'

#make layer from feature class
arcpy.MakeFeatureLayer_management("parcels", "lyr") 

# Select all cities which overlap the chihuahua polygon
arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", " [PROP_ID] = '18277' ")

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management("lyr", "18277protest_test")
