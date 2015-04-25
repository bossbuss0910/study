#coding= utf-8

import re
import os
import json


current_dir="~/amazon_review"
input_filename=current_dir+"/price_review.json"
output_filename=current_dir+"/price_sence_rate.txt"
expensive_list=["expensive"]
cheap_list=["cheap"]

def sentence_split(target):
	word_list=[]
	word_list=re.split(r'\s|\,|\.|\(|\)', target.lower())
	return word_list

def price_sence(price_review_dic):
	price_sence_dic={}
	for price,review in price_review_dic.items():
		e_count=0
		c_count=0
		review_num=0
		for sentence in review:
			review_num+=1
			check_count=0
			if len(list(set(expensive_list)&set(sentence_split(sentence))))>0:
				e_count=e_count+1
				check_count=check_count+1
			if len(list(set(cheap_list)&set(sentence_split(sentence))))>0:
				c_count=c_count+1
				check_count=check_count+1
			if check_count==2:
				print sentence
				c_count-=1
				e_count-=1
		price_sence_dic[price]=[e_count,c_count,review_num]
	print price_sence_dic
	return price_sence_dic

def price_match(dic):
	price_review_dic={}
	for i_id,price_dic in dic.items():
		for price,review in price_dic.items():
			if price not in price_review_dic:
				price_review_dic[price]=review
			else:
				price_review_dic[price].extend(review)
	return price_review_dic

def input_file(path):
	with open(path,'r') as f:
		dic =json.load(f)
	return dic
	
def output_file(dic,path):
	f=open(path,"w")
	for price in sorted(dic.keys()):
		if dic[price][0]+dic[price][1]!=0:
			print len(dic[price])
			out_str=str(price)+" "
			for number in dic[price]:
				out_str += str(number)+" "
			f.write(out_str.strip()+"\n")
	f.close()

def output_rate_file(dic,path):
	f=open(path,"w")
	for price in sorted(dic.keys()):
		if dic[price][0]+dic[price][1]!=0:
			out_str=str(price)+" "
			for number in range(2):
				out_str += str(float(dic[price][number])/dic[price][2])+" "
			f.write(out_str.strip()+"\n")
			print out_str.strip()+"\n"
	f.close()	

def main():
	file_path=os.path.expanduser(input_filename)
	outfile_path=os.path.expanduser(output_filename)

	itemid_dic=input_file(file_path)
	price_review=price_match(itemid_dic)
	price_sence_dic=price_sence(price_review)
	ex_num=0
	ch_num=0
	price_list=[]
	price_sence_dic2={}
	for price,num_list in price_sence_dic.items():
		price_list.append(float(price))
		price_sence_dic2[float(price)]=num_list
		ex_num+=num_list[0]
		ch_num+=num_list[1]
		if sum(num_list)!=0:
			print price
			print num_list
	price_list.sort()
	print "low:%f	high:%f	ave:%f"%(price_list[0],price_list[len(price_list)-1],sum(price_list)/len(price_list))
	print "expensive:%d	cheap:%d"%(ex_num,ch_num)
	output_rate_file(price_sence_dic2,outfile_path)

if __name__=="__main__":
	main()

