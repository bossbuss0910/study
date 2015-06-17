#coding: utf-8

import os

meta_file="dic/amazon_review/metadata.json"
review_file="dic/amazon_review/reviews_Amazon_Instant_Video.json"
def file_input(file):
	f=open(file)
	data=f.read()
	lines=data.split("\n")
	return lines

def mining_meta(metas):
	dic={}
	for data in metas:
		if "price" in data:
			print "ID:%s	price:%s" % (data["asin"],data["price"]
			dic[data["asin"]]=float(data["price"])
	print dic
	return dic

def mining_review(datas):
	dic={}
	for data in datas:
		if data["asin"] in dic.keys:
			dic[data["asin"]]=[]
			dic[data["asin"]].append(data["reviewText"])
		else:
			dic[data["asin"]]=data["reciewText"]
	print dic
	return dic

def main():
	meta_path = os.path.abspath(meta_file)
	review_path = os.path.abspath(review_file)
	
	meta_list=[]
	meta_list=file_input(meta_path)
	
	review_list=[]
	review_list=file_input(review_path)
	
	meta_dic={}
	review_dic={}
	meta_dic=mining_meta(meta_list)
	review_dic=mining_review(review_dic)

if __name__ == "__main__":
	main()




