#coding: utf-8

import os
import json
import gzip

current_dic="~/amazon_review"
meta_file=current_dic+"/metadata.json.gz"
review_file=current_dic+"/reviews_Apps_for_Android.json.gz"
output_file="/price_review_music.json"

def parse(path):
	g=gzip.open(path,"r")
	for l in g:
		yield eval(l)

def mining_meta(path):
	dic={}
	count=0
	tar=0
	for meta in parse(path):
		count=count+1
		if 'price' in meta:
			tar=tar+1
			dic[meta['asin']]=meta['price']
	print 'item:%d	tar:%d'%(count,tar)
	return dic

def mining_review(path):
	dic={}
	for data in parse(path):
		dic[data['asin']]=[]
		dic[data['asin']].append(data['reviewText'])
	return dic

def output_json(dic):
	with open(os.path.expanduser(current_dic+"/price_review_apps.json"),'w') as f :
		json.dump(dic, f,sort_keys=True,indent=4)

def matching(meta,review):
	match_dic={}
	for r_K,r_V in review.items():
		if r_K in meta:
			match_dic[r_K]={}
			match_dic[r_K][meta[r_K]]=r_V
	return match_dic	
			
def main():
	meta_path = os.path.expanduser(meta_file)
	review_path = os.path.expanduser(review_file)
	ratings=[]
	print meta_path

	meta_dic={}
	review_dic={}
	meta_dic=mining_meta(meta_path)
	review_dic=mining_review(review_path)

	match_dic={}
	match_dic=matching(meta_dic,review_dic)
	
	output_json(match_dic)

if __name__ == "__main__":
	main()




