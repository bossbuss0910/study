from gensim.models import word2vec
input_file="video3.txt"
ex_word="expensive"
ch_word="cheap"

data=word2vec.Text8Corpus(input_file)
model = word2vec.Word2Vec(data,size=100,window=5,min_count=10)

out_ex=model.most_similar(ex_word)
out_ch=model.most_similar(ch_word)

ex_list=["expensive"]
for word in out_ex:
	ex_list.append(word[0])

print ex_list
ch_list=["cheap"]
for word in out_ch:
	ch_list.append(word[0])

u_list=list(set(ex_list) & set(ch_list))

print u_list

print ex_word
for x in out_ex:
	if x[0] not in u_list:
		print x[0],x[1]
print "\n"
print ch_word
for x in out_ch:
	if x[0] not in u_list:
		print x[0],x[1]


