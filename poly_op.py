#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Build the class for polynomial operations"""


class Polynomial():
    def __init__(self, power=[]):
        """Input the coefficients of polynomial"""
        self.poly = {}
        for i in range(len(power)):
            self.poly[i] = power[len(power) - 1 - i]

    def __getitem__(self, key):
        if key in self.poly.keys():
            return self.poly[key]
        if key not in self.poly.keys():
            return 0

    def __setitem__(self, key, value):
        self.poly[key] = value

    def __add__(self, value):
        """add operation"""
        a1 = self.poly.copy()
        a2 = value.poly.copy()
        addd = {}
        ne = Polynomial([])
        for i in self.poly.keys():
            if i not in value.poly.keys():
                a2[i] = 0
        for i in value.poly.keys():
            if i not in self.poly.keys():
                a1[i] = 0
        for t in a1.keys():
            addd[t] = a1[t] + a2[t]
        for i in addd.keys():
            if addd[i] != 0:
                ne.poly[i] = addd[i]
        return ne

    def __mul__(self, va):
        """multiply"""
        a3 = self.poly.copy()
        a4 = va.poly.copy()
        mull = Polynomial([])
        tp = {}
        for i in self.poly.keys():
            tp[i] = 0
        for i in va.poly.keys():
            tp[i] = 0
        for i in self.poly.keys():
            for j in va.poly.keys():
                tp[i + j] = 0
        for i in self.poly.keys():
            for j in va.poly.keys():
                tp[i + j] = tp[i + j] + a3[i] * a4[j]
        for i in tp.keys():
            if tp[i] != 0:
                mull.poly[i] = tp[i]
        return mull

    def __eq__(self, ell):
        """assert if 2 polynomials are equal"""
        eqq = False
        f1 = {}
        f2 = {}
        l1 = []
        l2 = []
        ll = 0
        for i in self.poly.keys():
            if self.poly[i] != 0:
                f1[i] = self.poly[i]
        for i in ell.poly.keys():
            if ell.poly[i] != 0:
                f2[i] = ell.poly[i]
        if len(f1) == len(f2):
            l1 = list(sorted(f1.keys()))
            l2 = list(sorted(f2.keys()))
            if l1 == l2:
                for i in f1.keys():
                    if f1[i] == f2[i]:
                        ll = ll + 1
                if ll == len(f1):
                    eqq = True
        return eqq

    def __sub__(self, val):
        a5 = self.poly.copy()
        a6 = val.poly.copy()
        subb = {}
        sub = Polynomial([])
        for i in self.poly.keys():
            if i not in val.poly.keys():
                a6[i] = 0
        for i in val.poly.keys():
            if i not in self.poly.keys():
                a5[i] = 0
        for t in a5.keys():
            subb[t] = a5[t] - a6[t]
        for i in subb.keys():
            if subb[i] != 0:
                sub.poly[i] = subb[i]
        return sub

    def deriv(self):
        """derivative"""
        d = self.poly.copy()
        der = {}
        de = {}
        derr = Polynomial([])
        for i in d.keys():
            if i != 0:
                der[i] = d[i]

        for i in der.keys():
            de[i - 1] = der[i] * i
        for i in de.keys():
            if de[i] != 0:
                derr.poly[i] = de[i]
        return derr

    def eval(self, num):
        ee = 0
        e = self.poly.copy()
        for i in e.keys():
            ee = ee + e[i] * num**i
        return ee

def main():
    pass

if __name__ == "__main__":
    main()
