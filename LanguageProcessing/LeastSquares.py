# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as LA


#分散値
S=0.1
#次元数
D=2.0
#正則化項のパラメータ
k=0

#ベイズ線形回帰におけるガウスのパラメータ
alpha = 0.1 
beta = 9.0 


#x**iの基底関数
def phi2(x):
    f=[1]
    for i in np.arange(1,D):
        f.append(np.power(x,i))
    return f



#ガウスの基底関数
def gaussian_basis_func(s, mu):
        return lambda x:np.exp(-(x - mu)**2 / (2 * s**2))
def gaussian_basis_funcs(s, xs):
        return [gaussian_basis_func(s, mu) for mu in xs]
xs = np.arange(D)/D # D points
bases = gaussian_basis_funcs(S, xs)
def phi(x):
        return np.array([basis(x) for basis in bases])


def main(X,Y):
    PHI = np.array([phi2(x) for x in X])
    print PHI
   # PHI_G = np.array([phi(x) for x in X])
    #単位行列
    I = np.matrix(np.identity(D))
    #線形回帰
    print np.dot(PHI.T, PHI)
    w = np.linalg.solve(I*k+np.dot(PHI.T, PHI), np.dot(PHI.T, Y))     
    #線形回帰(ガウス)
    #w_G = np.linalg.solve(I*k+np.dot(PHI_G.T, PHI_G), np.dot(PHI_G.T, Y)) 
    #ベイズ線形回帰
    #Sigma_N = np.linalg.inv(alpha * np.identity(PHI_G.shape[1]) + beta * np.dot(PHI_G.T, PHI_G))
   # print Sigma_N
    #mu_N = beta * np.dot(Sigma_N, np.dot(PHI_G.T, Y))


    xlist = np.arange(0, 1, 0.01)
 #   plt.plot(xlist, [np.dot(w_G, phi(x)) for x in xlist], 'g') 
  #  plt.plot(xlist, [np.dot(mu_N, phi(x)) for x in xlist], 'b') 
    plt.plot(xlist, [np.dot(w, phi2(x)) for x in xlist], 'r') 
    
    plt.plot(X, Y, 'o')
    st=[]
    i=0
    for s in w:
        st.append(str(s)+"x**"+str(i))
        i+=1
    plt.title("f(x)="+"+".join(st),fontsize=15)
    plt.show()
if __name__ == '__main__':
    main()
