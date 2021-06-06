# Npz-extractor attempt by Artur Sahakyan

import numpy as np
import os

current_dir = os.getcwd()

def extract(filename):
	compress = np.load(str(filename),allow_pickle=True)
	#print(compress.files)
	os.makedirs(str(filename)[:-4]) 
	for file in compress.files:
		print(file)
		print(compress[str(file)])   
		np.save(os.path.join(str(filename)[:-4],str(file)+'.npy'),compress[str(file)])


for file in os.listdir():
	if file.endswith('.npz'):
		extract(file)
		print(file)