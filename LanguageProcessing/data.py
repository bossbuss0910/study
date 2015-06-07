#coding=utf-8
from collections import Counter
word_data=[]

def file_input(path):
	f=open(path)
	word_list=[]
	for line in f:
		word_list=line.split(",")
		for index in range(2,len(word_list)):
			word_data.append(word_list(index))
		word_list=[]
	f.close()

for index in range(1,51):
	input_filename='output/wordlist%d.txt'%index
	input_path = os.path.abspath(input_filename)
	file_input(input_path)
counter = Counter(word_data)
for word, cnt in counter.most_common():
	    print word, cnt
