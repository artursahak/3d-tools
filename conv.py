import numpy as np
import sys
import os
from stl import mesh

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders




#my_list = fast_scandir('.')
my_list = os.listdir()
print(my_list)
#exit()


for currFolder in my_list:
    try:
        verticesData = np.load(currFolder + '\\' +  'vertices.npy')
        facesData = np.load( currFolder + '\\' +  'faces.npy')

        fullVert = []
        fullFace = []
        #fileMesh = open("generatedMesh.xyz","w")
        for vert in verticesData:
       # currVertStr = 'v' + ' ' + str(vert[0]) + ' ' + str(vert[1]) + ' ' + str(vert[2])
            currVertStr = str(vert[0]) + ' ' + str(vert[1]) + ' ' + str(vert[2])
            tmpElAp = [vert[0],vert[1],vert[2]]
            fullVert.append(tmpElAp)
       # currVertStr =  str(vert[0]) + ' ' + str(vert[1]) + ' ' + str(vert[2]) 
       # fileMesh.write((currVertStr))
       # fileMesh.write("\n")



    #print("vertex count")
    #print(len(verticesData))
        currentIndex = 0	
        for faces in facesData:
            currentIndex += 1
       # if currentIndex % 2 == 0:
       #     continue
            currFaceStr = 'f'
        #for tmpEl in faces:
            tmpElAp = [faces[0],faces[1],faces[2]]
            fullFace.append(tmpElAp)
            currFaceStr = currFaceStr + ' ' +  str(faces[0])
            currFaceStr = currFaceStr + ' ' +  str(faces[1])
            currFaceStr = currFaceStr + ' ' +  str(faces[2])
        #fileMesh.write((currFaceStr))
        #if currentIndex != len(facesData):
         #   fileMesh.write("\n")
        fullVertNp = np.array(fullVert)
        fullFaceNp = np.array(fullFace)
    #print(fullVertNp)

        cube = mesh.Mesh(np.zeros(fullFaceNp.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(fullFaceNp):
            for j in range(3):
                cube.vectors[i][j] = fullVertNp[f[j],:]
        currentMeshName = currFolder + '\\' + currFolder + ".stl" 
        cube.save(currentMeshName)

        print(len(facesData))
    except:
        print("An exception occurred")	
#fileMesh.close()