#coding= utf-8

import re
import os
import json


input_filename="video_price.json"
output_filename="price_sence_rate_test.txt"
expensive_list=["expensive","entertaining","daughter","well"]
cheap_list=["cheap","quality","video","half"]

def sentence_split(target):
	word_list=[]
	word_list=re.split(r'\s|\,|\.|\(|\)', target.lower())
	return word_list

def price_sence(price_review_dic):
	price_sence_dic={}
	classfi_count = 0
	for price,review in price_review_dic.items():
		e_count=0
		c_count=0
		review_num=0
		for sentence in review:
			review_num+=1
			check_count=0
			if len(list(set(expensive_list)&set(sentence_split(sentence))))>0:
				print list(set(expensive_list)&set(sentence_split(sentence)))
				print sentence
				e_count=e_count+1
				check_count=check_count+1
			if len(list(set(cheap_list)&set(sentence_split(sentence))))>0:
				print list(set(cheap_list)&set(sentence_split(sentence)))
				print sentence
				c_count=c_count+1
				check_count=check_count+1
			if check_count==2:
				if len(list(set(expensive_list)&set(sentence_split(sentence))))>len(list(set(cheap_list)&set(sentence_split(sentence)))):
#					print sentence
					c_count-=1
				elif len(list(set(expensive_list)&set(sentence_split(sentence))))<len(list(set(cheap_list)&set(sentence_split(sentence)))):
					e_count-=1
				else:
					c_count-=1
					e_count-=1
		price_sence_dic[price]=[e_count,c_count,review_num]
	return price_sence_dic
'''
def price_match(dic):
	price_review_dic={}
	for i_id,price_dic in dic.items():
		for price,review in price_dic.items():
			if price not in price_review_dic:
				price_review_dic[price]=review
			else:
				price_review_dic[price].extend(review)
	return price_review_dic
'''
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
	sum_p=0
	for price in sorted(dic.keys()):
		sum_p+=dic[price][2]
		if dic[price][0]+dic[price][1]!=0:
			out_str=str(price)+" "
			for number in range(2):
				out_str += str(float(dic[price][number])/dic[price][2])+" "
			f.write(out_str.strip()+"\n")
	print sum_p
	f.close()	

def main():
	#file_path=os.path.expanduser(input_filename)
	#outfile_path=os.path.abspath(output_filename)
	#dirname=os.path.dirname(os.path.abspath(__file__))
	price_review=input_file(input_filename)
#	price_review=price_match(itemid_dic)
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
	price_list.sort()
	print "low:%f	high:%f	ave:%f"%(price_list[0],price_list[len(price_list)-1],sum(price_list)/len(price_list))
	print "expensive:%d	cheap:%d"%(ex_num,ch_num)
	output_rate_file(price_sence_dic2,output_filename)

if __name__=="__main__":
	main()

