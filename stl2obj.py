import bpy
import os
items = os.listdir("D:\\Dataset\\train\\allstl")

fileLoc = "D:\\Dataset\\train\\alstl"
for item in items:
	try:
	    if item.endswith(".stl"):   
	        bpy.ops.import_mesh.stl(filepath=os.path.join(fileLoc,str(item)),filter_glob='*.stl')
	        #print(item)
	        target_file = os.path.join("D:\\Dataset\\train\\allobj", str(item).split(".")[0]+".obj")
	        print(target_file)
	        bpy.ops.export_scene.obj(filepath=target_file)
	        for item in bpy.data.meshes:
	            bpy.data.meshes.remove(item)
    except:
    	print("Filename exception occurred")