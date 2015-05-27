# -*- coding: utf-8 -*-
import MeCab as mecab
import os

def wakati(text):
	#マイニングする品詞
	mining=["名詞","形容詞"]
	wakati=[]
	tagger = mecab.Tagger("-Ochasen")
	node = tagger.parseToNode(text)
	while node:
		if node.feature.split(",")[0] in mining:
			wakati.append(node.surface)
		node = node.next
	return wakati

def ngram(word_list,N):
	list=[]
	print len(word_list)
	for i in range(0,len(word_list)):
		if i+N-1>=len(word_list):
			break
		n_gram=[]
		for k in range(i+i+N):
			n_gram.append(word_list[k])
		list.append(set(n_gram))
	for set_word in list:
		print ",".join(set_word)

def main(N,text):
	list = []
	list = wakati(text)
	ngram(list,N)

if __name__ == "__main__":
	home = os.path.expanduser('~')
	dic = os.path.join(home,'Documents','study','LanguageProcessing','dic')

	filename='review1.txt'

	text = os.path.join(dic,filename)
	f=open(text)
	text=f.read()
	main(3,text)
	
