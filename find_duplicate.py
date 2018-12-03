#!usr/bin/env python
# -*- coding: utf-8 -*-

"""FAST find duplicated images, which might be translated, rotated, mirrored..."""


import sys
from os import listdir
import re
from skimage.io import imread
import numpy as np
from hashlib import sha256


def simp(data):
    """Extract the non-zero pixels"""
    s_v = np.nonzero(data < 1)
    min0 = min(s_v[0])
    min1 = min(s_v[1])
    max0 = max(s_v[0])
    max1 = max(s_v[1])
    daaa = np.zeros((max0 - min0 + 1, max1 - min1 + 1))
    for i in range(len(s_v[0])):
        daaa[s_v[0][i] - min0, s_v[1][i] -
             min1] = data[s_v[0][i]][s_v[1][i]]
    return daaa


def rot90(mat):
    """rotate a matrix by 90 degree"""
    t_u = mat.shape
    turn = np.zeros((t_u[1], t_u[0]))
    for i in range(t_u[1]):
        for j in range(t_u[0]):
            turn[i][j] = mat[t_u[0] - 1 - j][i]
    return turn


def tum(t_u):
    if t_u[0] <= t_u[1]:
        return t_u
    else:
        return (t_u[1], t_u[0])


def print_result(inpu):
    row_result = []
    for group in inpu:
        inpu = sorted(group, key=lambda x: int(re.sub(r'\D', '', x)))
        row_result.append(inpu)
    result = sorted(row_result, key=lambda x: int(re.sub(r'\D', '', x[0])))
    return result


class Pic():

    def __init__(self, name):
		"""Read the images as grey level"""
        self.name = name
        self.mat = simp(imread(name, as_grey=True))
        self.flag = 0
        self.t_r = {}

    def setv(self):
        self.t_r[0] = self.mat.copy()
        for i in range(1, 4):
            self.t_r[i] = rot90(self.t_r[i - 1])
        self.t_r[4] = np.transpose(self.t_r[0])
        for j in range(5, 8):
            self.t_r[j] = rot90(self.t_r[j - 1])

    def __eq__(self, va):
        for i in self.t_r:
            if np.array_equal(self.t_r[i], va.mat) is True:
                return True
        return False


def main():
    ORI = {}
    LST = []
    FI = []

    for file_name in listdir():
        if ".png" in file_name:
            obb = Pic(file_name)
            LST.append(obb)
            ORI[tum(obb.mat.shape)] = []
    for ob in LST:
        ORI[tum(ob.mat.shape)].append(ob)

    IDEXL = 0

    for shp in ORI:
        ii = 0
        jj = 0
        l_en = len(ORI[shp])
        while ii < l_en:
            t_ii = ORI[shp][ii]
            if t_ii.flag != 0:
                ii += 1
                continue
            else:
                FI.append([])
                FI[IDEXL].append(t_ii.name)
                t_ii.flag = 1
                t_ii.setv()

            while jj < l_en:
                t_jj = ORI[shp][jj]
                if ii < jj:
                    if ORI[shp][ii] == t_jj:
                        FI[IDEXL].append(t_jj.name)
                        t_jj.flag = 1
                jj += 1
            jj = 0
            ii += 1
            IDEXL += 1

    with open(sys.argv[1], 'w') as w_f:
        REE = ''
        for item in print_result(FI):
            t_m = "%s\n" % " ".join(item)
            w_f.write(t_m)
            REE += t_m
        print(sha256(REE.encode('utf-8')).hexdigest())


if __name__ == "__main__":
    main()
