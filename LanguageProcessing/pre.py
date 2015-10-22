#coding=utf-8
import re
import json

tar=["price","cost","price!","expensive","cheap"]

input_file="video_price.txt"
output_file="video_price2.txt"
f=open(input_file)
out=open(output_file,'w')
price_dic={}
for line in f:
	line_word=line.split(" ")
	price=line_word[0]
	del line_word[0]
	if len(list(set(line_word)&set(tar)))>0:
		line2=line.replace(",","").replace(".","").replace("[0-9]","")
		line2 = re.sub(r'[0-9]+', '', line2)
		if price not in price_dic:
			price_dic[price]=[line2]
		else:
			price_dic[price].append(line2)
		out.write(price+" "+line2)
f.close()
out.close()

with open('video_price.json','w') as f:
	json.dump(price_dic,f,sort_keys=True,indent=4)

