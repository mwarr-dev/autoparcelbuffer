# Import system modules
import arcpy

# Set the workspace
arcpy.env.workspace = 'F:\MWARREN\_scratch\_scratch.gdb'

# Select all cities which overlap the chihuahua polygon
chihuahua_cities = arcpy.SelectLayerByLocation_management('cities', 'INTERSECT', 
                                                          'chihuahua', 0, 
                                                          'NEW_SELECTION')

# Within selected features, further select only those cities which have a 
# population > 10,000   
arcpy.SelectLayerByAttribute_management(chihuahua_cities, 'SUBSET_SELECTION', 
                                        '"population" > 10000')

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(chihuahua_cities, 'chihuahua_10000plus')
