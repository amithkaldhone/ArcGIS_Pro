import arcpy
import datetime

startTime=datetime.datetime.now()

##Create Personal GDB
arcpy.CreatePersonalGDB_management(r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder',"gdb","10.0")

##Create Feature Dataset
arcpy.CreateFeatureDataset_management(r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb',"feature_dataset",r'C:\Users\amitk\Documents\ArcGIS_Practice\india.mdb\dataset\test_file')

##Copy Feature into Feature Dataset
arcpy.CopyFeatures_management(r'C:\Users\amitk\Documents\ArcGIS_Practice\india.mdb\dataset\test_file',r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp')

##Create Topology Layer
arcpy.CreateTopology_management(r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset',"topo_layer",0.00015)

##Add Feature Class into Topology Layer
arcpy.AddFeatureClassToTopology_management(r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\topo_layer',r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp',1,1)

##Add Topology Rules into Topology Layer
arcpy.AddRuleToTopology_management("topo_layer","Must Not Overlap (Area)",r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp',"",r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp',"")
arcpy.AddRuleToTopology_management("topo_layer","Must Not Have Gaps (Area)",r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp',"",r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset\demo_shp',"")


##Validate Topology Layer
arcpy.ValidateTopology_management("topo_layer","Full_Extent")
##Validation Completed!!")

##Create Topology Error layers
arcpy.ExportTopologyErrors_management("topo_layer",r'C:\Users\amitk\Documents\ArcGIS_Practice\New Folder\gdb.mdb\feature_dataset',"topo_errors")

arcpy.AddMessage("elapsed:\t"+str(datetime.datetime.now()-startTime))

arcpy.RefreshActiveView()