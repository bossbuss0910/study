# -*- coding: utf-8 -*-
import MeCab as mecab
import os

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

w_list=[]
def ngram(word_list,N):
	for i in range(0,len(word_list)):
		if i+N-1>=len(word_list):
			break
		n_gram=[]
		for k in range(i,i+N):
			n_gram.append(word_list[k])
		w_list.append(set(n_gram))

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


def main(N,text):
	list = []
	list = wakati(text)
	ngram(list,N)

if __name__ == "__main__":

	filename='dic/review1.txt'

	text = os.path.abspath(filename)
	text_list=text_split(text)
	for text in text_list:
		main(3,text)
	for set_word in w_list:
		if "価格" in set_word:
			print ",".join(set_word)
