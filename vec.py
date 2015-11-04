# -*- coding: utf-8 -*-
import os
from sklearn.svm import LinearSVC
import numpy as np

word_data=[]

def file_input(path):
	f=open(path)
	data=f.read()
	f.close()
	word_list=[]
	lines=data.split("\n")
	for line in lines:
		word_list=line.split(",")
		for index in range(2,len(word_list)):
			if word_list[index] not in ["値段","価格"]:
				word_data.append(word_list[index])
		word_list=[]
word_vec_c={}
word_vec_e={}
test_vec={}

def vec(word_vec,path):
	f=open(path)
	data=f.read()
	f.close()
	lines=data.split("\n")
	for line in lines:		
		word_vector=[0]*len(word_vec)
		word_list=line.split(",")
		for index in range(2,len(word_list)):
			if word_list[index] not in ["値段","価格"]:
				word_vector[word_vec.index(word_list[index])]=1
				if "安い" in word_list:
					word_vec_c.update({word_list[0]:word_vector})
				elif "高い" in word_list:
					print "高い"
					print word_list[0]
					word_vec_e.update({word_list[0]:word_vector})
				else:
					test_vec.update({word_list[0]:word_vector})

for index in range(12,13):
	input_filename='output/wordlist%d.csv'%index
	input_path = os.path.abspath(input_filename)
	file_input(input_path)
	word_vec=[]
	for word in set(word_data):
		word_vec.append(word)
	vec(word_vec,input_path)

	learn_vec=np.ones(len(word_vec))
	label_vec=[]
	for K,V in sorted(word_vec_c.items()):
		learn_vec=np.vstack([learn_vec,np.array(V)])
		label_vec.append(0)
	for K,V in sorted(word_vec_e.items()):
		learn_vec=np.vstack([learn_vec,np.array(V)])
		label_vec.append(1)
	learn_vec=np.delete(learn_vec,0,0)

	estimator = LinearSVC(C=1.0)
	estimator.fit(learn_vec,label_vec)
	print estimator
	test_data=np.ones(len(word_vec))
	for K,V in sorted(test_vec.items()):
		label_prediction=estimator.predict(np.array(V))
		print K
		print label_prediction
