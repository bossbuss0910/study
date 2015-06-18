#coding= utf-8

import re
import os

current_dir="~/amazon_review"
input_filename=current_dir+"/price_review.json"

expensive_list=["expensive"]
cheap_list=["cheap"]

def sentence_split(target):
	word_list=[]
	word_list=re.split(r'\s|\,|\.|\(|\)', target.lower())
	return word_list

def price_sence(price_review_dic):
	price_sence_dic={}
	print price_review_dic
	for price,review in price_review_dic.items():
		e_count=0
		c_count=0
		price_sence_list=[]
		for sentence in review:
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
			price_sence_list=[e_count,c_count]
		price_sence_dic[price]=price_sence_list
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
	print price_review_dic
	return price_review_dic

def input_file(path):

def main():
	file_path=os.path.expanduser(input_filename)
	itemid_dic={}
	itemid_dic=input_file(file_path)
	

if __name__=="__main__":
	main()


dic={"1":{"100":["this is cheap","expensive yeah!","cheap but expensive"]},"2":{"100":["this is cheap","expensive yeah!","cheap but expensive","expensive expensive"]}}
price_match(dic)
