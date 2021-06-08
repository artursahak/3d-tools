import os
import numpy as np
import os

current_dir = os.getcwd()

def extract(directory,filename):
	compress = np.load(str(filename),allow_pickle=True)
	#print(compress.files)
	os.makedirs(str(filename)[:-4]) 
	for file in compress.files:
		print(file)
		print(compress[str(file)])   
		np.save(directory + '\\' + str(file)+'.npy',compress[str(file)])

folders = os.listdir()

for folder in folders:
	content = os.listdir(folder)
	try:
		if not folder.endswith('.py'):
			#file_name = folder + ".npz"
			for sub in content:
				if sub.endswith(".npz"):
					print(folder + "\\" + sub)
					extract(folder,folder+"\\"+sub)
	except:
		print("Not a folder, but a python or other type of file occurred in loop")

	#if content.endswith('.npz'):
	#	print(content)