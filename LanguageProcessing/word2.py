#ioding= utf-8

import re
import os
import json


current_dir="~/amazon_review"
input_filename=current_dir+"/price_review_videos.json"
output_file="video_price.txt"

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
	
def out_file(dic):
	f=open(output_file,'w')
	for price,reviews in dic.items():
		for review in reviews:
			f.write(price+" "+review+"\n")
			print price+" "+review+"\n"
	f.close()


def main():
	file_path=os.path.expanduser(input_filename)
	print file_path
	itemid_dic=input_file(file_path)
	price_review=price_match(itemid_dic)
	out_file(price_review)

if __name__=="__main__":
	main()

