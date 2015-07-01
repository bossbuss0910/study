import matplotlib.pyplot as plt
import numpy as np
import os
import math
from sympy import *
from scipy.optimize import leastsq


parameter0=[0.,0.]
parameter1=[0,0]

current_dic="/dic"
input_filename="price_sence_rate.txt"
split_num=30


def file_input(path):
	f=open(path)
	data=f.read()
	line=data.split("\n")
	del line[len(line)-1]
	return line


def data_input(data):
	X=[]
	expensive=[]
	cheap=[]
	for index,line in enumerate(data):
		values=line.split(" ")
		X.append(float(values[0]))
		expensive.append(float(values[1]))
		cheap.append(float(values[2]))
	return X,expensive,cheap

def split_data(price,expensive,cheap):
	sep_num=len(price)/split_num
	index=0
	X=[]
	expensive_list=[]
	cheap_list=[]
	while index<=len(price):
		x_list=[]
		ex_list=[]
		ch_list=[]
		for k in range(sep_num):
			if index+1>len(price)-1:
				break
			index=index+1
			x_list.append(price[index])
			ex_list.append(expensive[index])
			ch_list.append(cheap[index])
		if len(x_list)==0:
			break
		x_list_ave=sum(x_list)/len(x_list)
		ex_list_max=max(ex_list)
		ch_list_max=max(ch_list)
		print x_list_ave,ex_list_max,ch_list_max
		X.append(x_list_ave)
		expensive_list.append(ex_list_max)
		cheap_list.append(ch_list_max)
	return X,expensive_list,cheap_list
	


def fit_func(parameter,x,y):
	a=parameter[0]
	b=parameter[1]
	residual = y - (a * np.exp(b * x))
	#residual=y-(a*x+b)
	return residual


file_path=os.path.expanduser(input_filename)
lis=file_input(file_path)
X,expensive,cheap=data_input(lis)
X,expensive,cheap=split_data(X,expensive,cheap)

print X
print expensive
print cheap

Px=np.array(X)
Py=np.array(expensive)
result=leastsq(fit_func,parameter0,args=(Px,Py))
ex=result[0]

Px=np.array(X)
Py=np.array(cheap)
result=leastsq(fit_func,parameter1,args=(Px,Py))
ch=result[0]
a=ex[0]
b=ex[1]
c=ch[0]
d=ch[1]
print b
print d

x = np.arange(0, 60, 5)
exp_ex = a*np.exp(b*x)
exp_ch = c*np.exp(d*x)
plt.plot(x, exp_ex,"-o",lw=2,alpha=0.7)
plt.plot(x,exp_ch,"-o",lw=2,alpha=0.7)

opt_price=(math.log(a)-math.log(c))/(d-b)

print opt_price

plt.show()
