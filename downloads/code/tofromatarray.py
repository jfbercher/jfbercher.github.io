# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:43:01 2014

@author: bercherj
"""

def tomat(*Z):
    """Converts the list of arrays in *Z to matrices"""
    Out=[]
    for iter in Z:
        iter=mat(iter)
        Out.append(iter)
    return Out
    
def toarray(*Z):
    """Converts the list of matrices in *Z to arrays"""
    Out=[]
    for iter in Z:
        iter=array(iter)
        Out.append(iter)
    return Out   
    
if __name__ == '__main__':
    A=randn(10,10)
    B=randn(7,14)
    C=[1, 3, 4]
    D,E,F=tomat(A,B,C)
    print(type(D))
    G,H,L=toarray(D,E,F)
    print(type(L))
    #
    A,B,C=tomat(A,B,C)
    print(type(A))
