# coding=utf-8 -*-
import os
import MeCab
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
encoding= "UTF-8"
token_dict=[]

def tokenize(text):
	walkati=MeCab.Tagger("-O wakati")
	return wakati.parse(text)

def fileread(tar_dir):
	for sudir,dirs,files in os.walk(tar_dir):
		for file in files:
			file_path = os.path.join(sudir,file)
			shake=codecs.open(file_path,'r',encoding)
			print shake
			text=shake.read(-1)
			lowers=text.lower()
			token_dict.append(lowers)
			file.close()
	return token_dict

def main():

	home = os.path.expanduser('~')
	dic = os.path.join(home,'Documents','study','LanguageProcessing','dic')
	#ファイルの読み込み
	token_dict=fileread(dic)
	print token_dict
	tfidf=TfidfVectorizer(tokenizer=tokenize,stop_words='english')
	tfs =tfidf.fit_transform(token_dict)

	print token_dict
	print tfs.toarray()

if __name__ =='__main__':
	main()

