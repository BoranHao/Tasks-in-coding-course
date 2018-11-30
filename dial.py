#!usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import scipy.signal as signal
import wave
import math
import scipy.io.wavfile as wavfile

"""Generate telephone dial sound using the numbers input"""


def dialer(file_name, frame_rate, phone, tone_time):

    p = phone
    pp = []
    for i in range(len(p)):
        pp.append(p[i])
        pp[i] = int(pp[i])
    # print(pp)
    channels = 1
    sampwidth = 2

    #tone_time = 1
    time = tone_time
    vol = 8000

    t = np.arange(0, time, 1 / frame_rate)
    # print(t)

    a1 = signal.chirp(t, 697, time, 697, method='linear') * vol
    # print(a1[1])
    a11 = t.copy()
    for i in range(len(t)):
        a11[i] = math.cos(2 * np.pi * 697 * t[i]) * vol

    #a11 = a11.astype(np.short)
    # print(a11[1])
    # print(a1[2])
    b1 = signal.chirp(t, 1209, time, 1209, method='linear') * vol
    #b1 = b1.astype(np.short)
    n1 = a11 + b1
    #n1 = n1.astype(np.short)

    a2 = signal.chirp(t, 697, time, 697, method='linear') * vol
    #a2 = a2.astype(np.short)
    b2 = signal.chirp(t, 1336, time, 1336, method='linear') * vol
    #b2 = b2.astype(np.short)
    n2 = a2 + b2
    #n2 = n2.astype(np.short)

    a3 = signal.chirp(t, 697, time, 697, method='linear') * vol
    #a3 = a3.astype(np.short)
    b3 = signal.chirp(t, 1477, time, 1477, method='linear') * vol
    #b3 = b3.astype(np.short)
    n3 = a3 + b3
    #n3 = n3.astype(np.short)

    a4 = signal.chirp(t, 770, time, 770, method='linear') * vol
    #a4 = a4.astype(np.short)
    b4 = signal.chirp(t, 1209, time, 1209, method='linear') * vol
    #b4 = b4.astype(np.short)
    n4 = a4 + b4
    #n4 = n4.astype(np.short)

    a5 = signal.chirp(t, 770, time, 770, method='linear') * vol
    #a5 = a5.astype(np.short)
    b5 = signal.chirp(t, 1336, time, 1336, method='linear') * vol
    #b5 = b5.astype(np.short)
    n5 = a5 + b5
    #n5 = n5.astype(np.short)

    a6 = signal.chirp(t, 770, time, 770, method='linear') * vol
    #a6 = a6.astype(np.short)
    b6 = signal.chirp(t, 1477, time, 1477, method='linear') * vol
    #b6 = b6.astype(np.short)
    n6 = a6 + b6
    #n6 = n6.astype(np.short)

    a7 = signal.chirp(t, 852, time, 852, method='linear') * vol
    #a7 = a7.astype(np.short)
    b7 = signal.chirp(t, 1209, time, 1209, method='linear') * vol
    #b7 = b7.astype(np.short)
    n7 = a7 + b7
    #n7 = n7.astype(np.short)

    a8 = signal.chirp(t, 852, time, 852, method='linear') * vol
    #a8 = a8.astype(np.short)
    a88 = t.copy()
    for i in range(len(t)):
        a88[i] = math.sin(2 * np.pi * 852 * t[i]) * 2 * vol
    b8 = signal.chirp(t, 1336, time, 1336, method='linear') * vol
    #b8 = b8.astype(np.short)
    b88 = t.copy()
    for i in range(len(t)):
        b88[i] = math.sin(2 * np.pi * 1336 * t[i]) * 2 * vol
    n8 = a88 + b88
    #n8 = n8.astype(np.short)

    a9 = signal.chirp(t, 852, time, 852, method='linear') * vol
    #a9 = a9.astype(np.short)
    b9 = signal.chirp(t, 1477, time, 1477, method='linear') * vol
    #b9 = b9.astype(np.short)
    n9 = a9 + b9
    #n9 = n9.astype(np.short)

    a0 = signal.chirp(t, 941, time, 941, method='linear') * vol
    #a0 = a0.astype(np.short)
    a00 = t.copy()
    for i in range(len(t)):
        a00[i] = math.sin(2 * np.pi * 941 * t[i]) * 1.5 * vol
    b0 = signal.chirp(t, 1336, time, 1336, method='linear') * vol
    #b0 = b0.astype(np.short)
    b00 = t.copy()
    for i in range(len(t)):
        b00[i] = math.sin(2 * np.pi * 1336 * t[i]) * 1.5 * vol
    n0 = a00 + b00
    #n0 = n0.astype(np.short)

    n = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    nn = []
    dd = n[pp[0]]
    ii = 1
    while ii < len(pp):
        dd = np.hstack((dd, n[pp[ii]]))
        ii = ii + 1
    dd = dd.astype(np.int16)
    # print(dd)

    # open a wav document
    """f = wave.open(file_name,"wb")
	#set wav params
	f.setnchannels(channels)
	f.setsampwidth(sampwidth)
	f.setframerate(frame_rate)
	#turn the data to string
	f.writeframes(dd)

	f.close()"""

    wavfile.write(file_name, frame_rate, dd)


# dialer('sc',8000,'9123456780',0.15)

def main():
    pass


if __name__ == '__main__':
    main()
