#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Extract the loudest band in a sound track"""

import numpy as np
import sys
import scipy.signal as signal
import wave
import math
import matplotlib.pyplot as pyplot
FFT = np.fft


def loudest_band(music, frame_rate, bandwidth):
    nn00 = FFT.fft(music)

    t = np.arange(0, len(nn00) / frame_rate, 1.0 / frame_rate)

    n00 = abs(nn00)
    # n00[0]=0

    iv = frame_rate / len(n00)
    ivv = bandwidth / iv
    ivv = int(ivv)
    ray = []
    points = int(len(n00) / 2 - ivv)
    for i in range(0, int(len(n00) / 2 + 1)):
        ray.append(n00[i]**2)
    summ = [sum(ray[0:ivv])]
    for j in range(1, points + 1):
        summ.append(summ[j - 1] - ray[j - 1] + ray[j + ivv - 1])
    po = np.argmax(summ)

    # range(po,po+ivv+1)

    ou = np.zeros(len(nn00), dtype=complex)
    TT = t[len(nn00) - 1]
    ff = t * frame_rate / TT

    # posi=np.argmax(n00)
    if po != 0:
        for i in range(po, po + ivv + 1):
            ou[i] = nn00[i]
        for i in range(len(t) - po - ivv, len(t) - po + 1):
            ou[i] = nn00[i]
        ou[0] = nn00[0]
    if po == 0:
        ou[0] = nn00[0]
        for i in range(po + 1, po + ivv + 1):
            ou[i] = nn00[i]
        for i in range(len(t) - po - ivv, len(t) - po - 1 + 1):
            ou[i] = nn00[i]

    timedomin = FFT.ifft(ou)
    # print(timedomin)
    # timedomin=timedomin.astype(np.short)
    # print(len(timedomin))
    # pyplot.plot(ff,abs(ou))
    # pyplot.grid(True)
    # pyplot.show()

    #f = wave.open('out.wav',"wb")
    # set wav params
    # f.setnchannels(1)
    # f.setsampwidth(2)
    # f.setframerate(frame_rate)
    # f.writeframes(timedomin.tostring())

    # f.close()
    fi = (po * iv, iv * (po + ivv), timedomin)
    # print(fi)
    return fi


# loudest_band(music,8000,100)


def main():
    pass


if __name__ == '__main__':
    main()
