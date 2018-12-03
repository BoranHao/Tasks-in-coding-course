#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Given the length and some letters, QUICKLY find all words which contain those letters and are of the given length. Hash table is used"""
import sys
import itertools

FILENAME = sys.argv[1]
with open(FILENAME) as dicc:
    LINES = dicc.readlines()
LEE = len(LINES)
for j in range(LEE):
    LINES[j] = LINES[j].replace("\n", "")


def com(word):
    lst = sorted(set(list(word)))
    dik = "".join(lst)
    return dik


def sta(word):
    """Count how many times the letters in a word appear"""
    dik = {}
    for item in word:
        dik[item] = 0
    for i in word:
        dik[i] = dik[i] + 1
    return dik


STAA = {}
for item1 in range(30):
    STAA[item1] = {}
for line in LINES:
    STAA[len(line)][com(line)] = {}
for line in LINES:
    # Build a LARGE dictionary (hash table) to improve the search speed.
    STAA[len(line)][com(line)][line] = sta(line)


def main():
    while True:
        A = input()
        if A == "":
            break
        AA = A.split()
        LETTER = AA[0]
        LON = int(AA[1])
        if LON == 0:
            break
        MAX_OVERFLOW = []
        TAR = {}
        CCC = com(LETTER)
        TAR = sta(LETTER)
        RANN = min(LON, len(CCC))
        for i1 in range(1, RANN + 1):
            ITERA = itertools.combinations(CCC, i1)
            for j1 in list(ITERA):
                strr = "".join(j1)
                try:
                    for w in STAA[LON][strr]:
                        flag = 0
                        try:
                            indik = STAA[LON][strr][w]
                            for ww in indik:
                                if indik[ww] > TAR[ww]:
                                    flag = 1
                                    break
                        except KeyError:
                            continue
                        if flag == 0:
                            MAX_OVERFLOW.append(w)
                except KeyError:
                    continue
        for i2 in sorted(MAX_OVERFLOW):
            print(i2)
        print('.')


if __name__ == '__main__':
    main()
