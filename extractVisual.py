import streamlit as st


import numpy as np
import os

st.sidebar.write("Welcome to npz-extractor")
upload_file = st.file_uploader("Upload your .npz file",type=[".npz"])

current_dir = os.getcwd()

def extract(filename):
	compress = np.load(str(filename),allow_pickle=True)
	#print(compress.files)
	os.makedirs(str(filename)[:-4]) 
	for file in compress.files:
		print(file)
		print(compress[str(file)])   
		np.save(os.path.join(str(filename)[:-4],str(file)+'.npy'),compress[str(file)])

if upload_file is not None:
	st.write(upload_file.name)
	extract(upload_file.name)
	

