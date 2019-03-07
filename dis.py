#!/usr/bin/env python3


def Dinfty(a,b):
    '''
    dinfty
    '''
    return np.max(abs(a-b))

def D1(a,b):
    '''
    d_one
    '''
    return sum(abs(b-a))     

def D2(a,b):
    '''
    d_two
    '''
    return np.sqrt(sum(abs(b-a))**2)


def distmatrix(N, dist, x_train):
    D = np.zeros((N,N))
    for i, j in itertools.product(xrange(N), xrange(i,N)):
        D[i][j] = dist(x_train[i], x_train[j])
        D[j][i] = D[i][j]
    return D	  	 












































