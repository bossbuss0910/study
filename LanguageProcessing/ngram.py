# -*- coding: utf-8 -*-
import MeCab as mecab
import os


#分かち書き　名詞と形容詞のみを抽出
def wakati(text):
	#マイニングする品詞
	mining=["名詞","形容詞"]
	wakati_list=[]
	tagger = mecab.Tagger("-Ochasen")
	node = tagger.parseToNode(text)
	while node:
		if node.feature.split(",")[0] in mining:
			wakati_list.append(node.surface)
		node = node.next
	return wakati_list

#各reviewのマップ
user_map={}

#星の数
star_list=[]

#N_gram抽出
def ngram(word_list,N,review_id):
	w_list=[]
	for i in range(0,len(word_list)):
		if i+N-1>=len(word_list):
			break
		n_gram=[]
		for k in range(i,i+N):
			n_gram.append(word_list[k])
		w_list.append(set(n_gram))
	user_map[review_id]=w_list


#テキストデータの分割
def text_split(text):
	f=open(text)
	for k in range(0,1):
		f.readline()
	review_list=[]
	str=""
	line=f.readline()
	star_list.append(line[0])
	while line:
		if line.startswith('【review'):
			review_list.append(str)
			str=""
			line=f.readline()
			star_list.append(line[0])
		else:
			str=str+line
		line=f.readline()
	review_list.append(str)
	f.close()
	return review_list

#ファイル出力
def output_file(filename,output_list):
	f=open(filename,'w')
	for str in output_list:
		f.write(str+"\n")
	f.close()


def main(N,text,review_id):
	list = []
	list = wakati(text)
	ngram(list,N,review_id)

if __name__ == "__main__":

	input_filename='dic/review2.txt'
	output_filename='output/wordlist2.csv'
	#レビュー数
	review_number=0
	#値段or価格を含むレビュー数
	target_review=0

	text = os.path.abspath(input_filename)
	text_list=text_split(text)
	for index,text in enumerate(text_list):
		main(3,text,index)
	
	review_number=index
	#ファイルに書き込むためのリスト
	output_list=[]

	for K,V in user_map.items():
		word_list=[]
		for word_set in V:
			if "価格" in word_set or "値段" in word_set:
				target_review += 1
				for word in word_set:
					word_list.append(word)
		if len(word_list)!=0:
			output_list.append("{0},{1},{2}".format(K+1,star_list[K-1],",".join(set(word_list))))
	for s in output_list:
		print s

	output_filename=os.path.abspath(output_filename)

	output_file(output_filename,output_list)
	print "レビュー数:%d" %review_number
	print "値段・価格を含むレビュー数:%d" %target_review
