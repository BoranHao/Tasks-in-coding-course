#!usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import zeros, exp, array, pi

"""Fast Fourier transform"""
# x=8


"""a=array([(1,2+1j),(1,3)],dtype=complex)
b=array([1,2,3,4])
b=b.reshape((2,2))
c=a@b
print(a)
print(b)
print(c)
print(a)"""


def DFT(x):
    try:
        N = len(x)
        WN = exp(-(2 * pi * 1j) / N)
        A = zeros((N, N), dtype=complex)
        for i in range(N):
            for j in range(N):
                A[i][j] = WN**(i * j)
        X = A@x
        return X
    except BaseException:
        raise ValueError


print(DFT([1, 2, 3, 4, 5]))
# print(FFT.fft(x))


def main():
    pass


if __name__ == '__main__':
    main()
