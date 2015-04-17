# -*- coding: utf-8 -*-
import os
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

def vec(word_vec,path):
	f=open(path)
	data=f.read()
	f.close()
	word_vector=[0]*len(word_vec)
	lines=data.split("\n")
	for line in lines:
		word_list=line.split(",")
		if "安い" in word_list:
			for index in range(2,len(word_list)):
				if word_list[index] not in ["値段","価格"]:
					word_vector[word_vec.index(word_list[index])]=1
			word_vec_c.update({word_list[0]:word_vector})
		if "高い" in word_list:
			for index in range(2,len(word_list)):
				if word_list[index] not in ["値段","価格"]:
					word_vector[word_vec.index(word_list[index])]=1
			word_vec_e.update({word_list[0]:word_vector})

for index in range(1,2):
	input_filename='output/wordlist%d.csv'%index
	input_path = os.path.abspath(input_filename)
	file_input(input_path)
	word_vec=[]
	for word in set(word_data):
		print word
		word_vec.append(word)
	vec(word_vec,input_path)

	print"安い"
	for K,V in sorted(word_vec_c.items()):
		print "a"

	print"高い"
	for K,V in sorted(word_vec_e.items()):
		print "b"
