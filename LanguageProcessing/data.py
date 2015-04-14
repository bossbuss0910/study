#coding=utf-8
from collections import Counter
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
			word_data.append(word_list[index])
		word_list=[]

def file_output(path):
	f=open(path,"w")
	counter = Counter(word_data)
	for word, cnt in counter.most_common():
		print word,cnt
		f.write("{0},{1}\n".format(word,cnt))
	f.close()

for index in range(1,51):
	input_filename='output/wordlist%d.csv'%index
	input_path = os.path.abspath(input_filename)

	file_input(input_path)
	output_filename='output/wordcount.csv'
output_filename='output/wordcount.csv'
output_path= os.path.abspath(output_filename)
file_output(output_path)
