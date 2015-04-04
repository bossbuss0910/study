# coding=utf-8
# kmeansクラスタリング

import numpy as np
from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt

#クラスタ数
cluster=3

#回数
state=10

#データの生成
def data(n_point):
	X=np.random.normal(0,1,n_point)
	Y=np.random.normal(0,1,n_point)
	return np.c_[X,Y]
#クラスタリング
def kmeans(points):
	model=KMeans(n_clusters=cluster,random_state=state).fit(points)
	return model.labels_

if __name__ == '__main__':
	points=data(100)
#	print points
	labels=kmeans(points)
	for label,point in zip(labels,points):
		if label==0:
			plt.plot(point[0],point[1],"ro")
		if label==1:
			plt.plot(point[0],point[1],"go")
		if label==2:
			plt.plot(point[0],point[1],"bo")
	plt.show()
