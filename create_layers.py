# Import system modules
import arcpy, os, sys

# Import Environment
from arcpy import env

# Set the workspace
arcpy.env.workspace = r'F:\MWARREN\_scratch\_scratch.gdb'

#Make sure "ownership" layer is inside GDB

PROP_ID = input("Enter PROP_ID: ")
where_clause ='"PROP_ID" = ' + '{}'.format(PROP_ID)
distance = "200 Feet"

# Create selection of parcel with indicated input
parcel = arcpy.SelectLayerByAttribute_management("ownership", "NEW_SELECTION", where_clause)

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(parcel, "parcel{}".format(PROP_ID))

# Create selection of 200ft buffer around indicated parcel
buffer200 = arcpy.SelectLayerByLocation_management("ownership", 'INTERSECT', 'parcel{}'.format(PROP_ID), distance, 'NEW_SELECTION')

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(buffer200, "parcel{}_200ftbuffer".format(PROP_ID))


