#!usr/bin/env python
# -*- coding: utf-8 -*-

"""FAST solve the cellphone game 'WordBrain' using recursion"""
from sys import argv
import copy
import itertools
import numpy as np

FILENAME1 = argv[1]  # search  words  with wordplayer
FILENAME2 = argv[2]
with open(FILENAME1) as dicc1:
    LINES1 = dicc1.readlines()
LEE1 = len(LINES1)
for j in range(LEE1):
    LINES1[j] = LINES1[j].replace("\n", "")

with open(FILENAME2) as dicc2:
    LINES2 = dicc2.readlines()
LEE2 = len(LINES2)
for jj in range(LEE2):
    LINES2[jj] = LINES2[jj].replace("\n", "")


def com(word):
    lst = sorted(set(list(word)))
    dik = "".join(lst)
    return dik


def sta(word):
    dik = {}
    for item in word:
        dik[item] = 0
    for i in word:
        dik[i] = dik[i] + 1
    return dik


STAA1 = {}
for item1 in range(30):
    STAA1[item1] = {}
for line in LINES1:
    STAA1[len(line)][com(line)] = {}
for line in LINES1:
    STAA1[len(line)][com(line)][line] = sta(line)

STAA2 = {}
for item1 in range(30):
    STAA2[item1] = {}
for line in LINES2:
    STAA2[len(line)][com(line)] = {}
for line in LINES2:
    STAA2[len(line)][com(line)][line] = sta(line)
LK = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, 1), (0, -1), (1, -1), (-1, -1)]


def find(letter, lonn, ver):
    """Use the previous wordplayer to find potential words"""
    if ver == 1:
        staaa = STAA1
    else:
        staaa = STAA2
    lon = len(lonn)
    maxov = []
    ccc = com(letter)
    tar = sta(letter)
    rann = min(lon, len(ccc))
    for i in range(1, rann + 1):
        itera = itertools.combinations(ccc, i)
        for j_e in list(itera):
            strr = "".join(j_e)
            try:
                for w_o in staaa[lon][strr]:
                    flag = 0
                    try:
                        indik = staaa[lon][strr][w_o]
                        for w_w in indik:
                            if indik[w_w] > tar[w_w]:
                                flag = 1
                                break
                    except KeyError:
                        continue
                    if flag == 0:
                        maxov.append(w_o)
            except KeyError:
                continue
    yan = ''
    for i in range(lon):
        yan = yan + '*'

    if yan != lonn:
        ind = []
        for i in range(lon):
            if yan[i] != lonn[i]:
                ind.append(i)
        f_i = []
        for word in maxov:
            fla = 1
            for i_x in ind:
                if word[i_x] != lonn[i_x]:
                    fla = 0
                    break
                if fla == 1:
                    f_i.append(word)
        maxov = f_i
    return maxov


class Letter():
    """define the class to run recursion"""

    def __init__(self, mat, cor, lett, word, sublet=[], level=0, backletter=0):
        self.mat = mat
        self.level = level
        self.subletter = sublet
        self.backletter = backletter
        self.cor = cor
        self.lett = lett
        self.word = word


def findnab(letter):
    """Find neighbor letters"""
    suble = []
    t_u = letter.cor
    c_c = letter.mat.copy()
    w_e = letter.word
    lec = letter.level
    tur = w_e[lec + 1]
    for t_r in LK:
        try:
            t_1 = t_u[0] + t_r[0]
            t_2 = t_u[1] + t_r[1]
            w_v = c_c[t_1][t_2]
            if w_v == tur:
                if ((t_u[0] + t_r[0] >= 0) & (t_u[1] + t_r[1] >= 0)) == 1:
                    c_c[t_u[0]][t_u[1]] = ''
                    j_u = Letter(
                        c_c, (t_1, t_2), w_v, w_e, [], lec + 1, letter)
                    suble.append(j_u)
        except IndexError:
            pass
    return suble


def lettoblist(mat, word):  # initialized
    fii = []
    size = mat.shape[0]
    for iii in range(size):
        for jjj in range(size):
            if mat[iii][jjj] == word[0]:
                fii.append(Letter(mat, (iii, jjj), mat[iii][jjj], word))
    return fii


def setallsuble(obb, times):
    """Recursion"""
    if obb.subletter != []:
        for letter in obb.subletter:
            if letter.level != times - 1:
                letter.subletter = findnab(letter)
                setallsuble(letter, times)


REE = []


def search(obb, times):
    for o_b in obb.subletter:
        if o_b.level == times - 1:
            lsc = [o_b.cor]
            t_p = o_b.backletter
            for i in range(times - 1):
                lsc.insert(0, t_p.cor)
                t_p = t_p.backletter
            REE.append(lsc)
        else:
            search(o_b, times)


def findpath(mat, target):    # return a list of cordinates tuples
    fii = lettoblist(mat, target)
    ori = Letter(mat, (-1, -1), 1, target, fii)
    setallsuble(ori, len(target))
    search(ori, len(target))
    r_e = copy.deepcopy(REE)
    REE.clear()
    return r_e


def staa(mat):
    letters = ''
    jie = mat.shape[0]
    for i_k in range(jie):
        for j_k in range(jie):
            letters = letters + mat[i_k][j_k]
    return letters


class Path():

    def __init__(self, mat, word, cord, shapee, level=0, backpath=0):
        self.shapee = shapee
        self.word = word
        self.mat = mat
        self.cord = cord
        self.subpath = []
        self.backpath = backpath
        self.level = level
        self.letters = staa(mat)


def down(mat):
    """Simulate how will the letters collapse down"""
    t_u = mat.shape
    flag = 0
    for i_b in range(t_u[0] - 1):
        for j_b in range(t_u[0]):
            if (mat[i_b][j_b] != '') & (mat[i_b + 1][j_b] == '') == 1:
                mat[i_b + 1][j_b] = mat[i_b][j_b]
                mat[i_b][j_b] = ''
                flag = 1
    if flag != 0:
        down(mat)
    return mat


def removeletter(matt, cor):
    mat = matt.copy()
    for t_u in cor:
        mat[t_u[0]][t_u[1]] = ''
    return mat


def findsub(obb, ver):  # set one sub
    """FInd potential subpaths"""
    mxt = down(removeletter(obb.mat, obb.cord))
    rst = []
    worlist = find(staa(mxt), obb.shapee[obb.level], ver)
    for word in worlist:
        ppaths = findpath(mxt, word)  # de dao paths list
        if ppaths != []:
            for ppath in ppaths:
                o_b = Path(mxt, word, ppath, obb.shapee, obb.level + 1, obb)
                rst.append(o_b)
    obb.subpath = rst


FI = []


def printye(obb):
    """print  leaves"""
    for o_b in obb.subpath:
        if o_b.level == len(obb.shapee):
            t_p = [o_b.word]
            a_m = o_b.backpath
            for i in range(len(obb.shapee) - 1):
                t_p.insert(0, a_m.word)
                a_m = a_m.backpath
            FI.append(t_p)
        else:
            printye(o_b)


def setallsub(obb, shapee, ver):
    if obb.subpath != []:
        for o_b in obb.subpath:
            if o_b.level != shapee:
                findsub(o_b, ver)
                setallsub(o_b, shapee, ver)


def proc(ceo, shapee):
    o_b = Path(ceo, 'ori', [], shapee, 0)
    findsub(o_b, 1)
    setallsub(o_b, len(shapee), 1)
    printye(o_b)
    fib = []
    if FI == []:
        o_b = Path(ceo, 'ori', [], shapee, 0)
        findsub(o_b, 2)
        setallsub(o_b, len(shapee), 2)
        printye(o_b)
    [fib.append(i) for i in FI if i not in fib]
    fib = sorted(fib)
    for fibb in fib:
        for i in range(len(fibb) - 1):
            print(fibb[i], end=' ')
        print(fibb[len(fibb) - 1])
    print('.')
    FI.clear()


def main():
    while 1:
        try:
            a_a = input()
            if a_a == '':
                break
            jie = len(a_a)
            c_u = np.empty((jie, jie), dtype=str)
            for i in range(jie):
                for j_l in range(jie):
                    c_u[i][j_l] = ''
            for i in range(jie):
                c_u[0][i] = a_a[i]
            for i in range(jie - 1):
                linee = input()
                for j_x in range(jie):
                    c_u[i + 1][j_x] = linee[j_x]
            shape = input().split()
            proc(c_u, shape)
        except EOFError:
            break


if __name__ == "__main__":
    main()
