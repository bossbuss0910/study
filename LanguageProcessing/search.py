#coding: utf-8

import os

input_dict="dic/data/pen/price"
files=os.path.abspath(input_dict)

count =0

for file in files:
	f=open(file)
	data=f.read()
	lines = data.split("\n")
	if len(lines)==1:
		print file
		count++

