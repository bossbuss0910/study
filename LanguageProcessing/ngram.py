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
	while line:
		if line.startswith('【'):
			review_list.append(str)
			str=""
			line=f.readline()
		else:
			str=str+line
		line=f.readline()
	review_list.append(str)
	f.close()
	return review_list


def main(N,text,review_id):
	list = []
	list = wakati(text)
	ngram(list,N,review_id)

if __name__ == "__main__":

	filename='dic/review1.txt'

	text = os.path.abspath(filename)
	text_list=text_split(text)
	for index,text in enumerate(text_list):
		main(3,text,index)
	for K,V in user_map.items():
		word_set=[]
		print K
		for word_set in V:
			if "価格" in word_set:
				for word in word_set:
					word_list.append(word)
