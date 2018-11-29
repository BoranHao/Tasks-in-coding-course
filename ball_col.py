#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Given balls in 2d plain and their initial speed/position, predict their position at any time"""


import copy
import math
import sys
import os

class Ball():

	def __init__(self, nu, x, y, vx, vy):
		"""Initialize the speed and position of balls"""
		self.nu = nu
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def move(self, t):
		self.x = self.x + t * self.vx
		self.y = self.y + t * self.vy

	def pri(self):
		re = ''
		re = re + self.nu + ' ' + \
			str(self.x) + ' ' + str(self.y) + ' ' + \
			str(self.vx) + ' ' + str(self.vy)
		print(re)

	def coll(self, value):
		"""Movement after a 1-d collision"""
		yyy = ((self.vx - value.vx) * (self.x - value.x) + (self.vy - value.vy) * (self.y - value.y)
			   ) / ((self.x - value.x) * (self.x - value.x) + (self.y - value.y) * (self.y - value.y))
		vxx = self.vx
		vyy = self.vy
		self.vx = self.vx - yyy * (self.x - value.x)
		self.vy = self.vy - yyy * (self.y - value.y)

		value.vx = value.vx - yyy * (value.x - self.x)
		value.vy = value.vy - yyy * (value.y - self.y)

	def acolb(self, value):
		"""status after a 2-d collision"""
		q1 = self.vx - value.vx
		q2 = self.vy - value.vy
		p1 = value.x - self.x
		p2 = value.y - self.y
		if q1 * q1 + q2 * q2 == 0:
			ascol = 0
		if q1 * q1 + q2 * q2 != 0:
			dist = math.sqrt(pow((self.x - value.x), 2) +
							 pow((self.y - value.y), 2))
			cosxita = (p1 * q1 + p2 * q2) / (math.sqrt(p1 *
													   p1 + p2 * p2) * math.sqrt(q1 * q1 + q2 * q2))
			if cosxita <= 0:
				ascol = 0
			if cosxita > 0:
				A = dist * math.sqrt(1 - cosxita * cosxita)
				if A < 10:
					ascol = 1
				if A >= 10:
					ascol = 0
		return ascol

	def cotime(self, value):
		"""When will collision happen"""
		q1 = self.vx - value.vx
		q2 = self.vy - value.vy
		p1 = value.x - self.x
		p2 = value.y - self.y
		dist = math.sqrt(pow((self.x - value.x), 2) +
						 pow((self.y - value.y), 2))
		cosxita = (p1 * q1 + p2 * q2) / (math.sqrt(p1 * p1 +
												   p2 * p2) * math.sqrt(q1 * q1 + q2 * q2))
		ll = math.sqrt(100 - dist * dist * (1 - cosxita * cosxita))
		t = (dist * cosxita - ll) / (math.sqrt(q1 * q1 + q2 * q2))
		return t

bal = []
ball = []
time = []

# bal.append(Ball("mm1",0,-30,0,0))
# bal.append(Ball("mm2",0,9,0,0))
# bal.append(Ball("mm3",-60,10,0,0))


def main():
    for i in sys.argv[1:]:
        try:
            if float(i) >= 0:
                time.append(float(i))
                time = sorted(time)
        except ValueError:
            os._exit(2)

    if time == []:
        os._exit(2)

    stt = ''
    bal = []
    iu = 0
    try:
        while 1 > 0:
            line = sys.stdin.readline()
            if line == "":
                break
            if len(line.split()) != 5:
                os._exit(1)
            m = line.split()
            bal.append(
                Ball(
                    m[0], float(
                        m[1]), float(
                        m[2]), float(
                        m[3]), float(
                        m[4])))

    except ValueError:
        os._exit(1)
    except IndexError:
        os._exit(1)

    v1 = []
    v2 = []

    num = 1

    mt = []

    ct = 0
    i = 0
    blen = len(bal)

    while i < len(time):
        """Using recursion to run the movement"""
        ball = copy.deepcopy(bal)
        t = time[i]
        tc = 0

        while 1 > 0:
            num = 1
            ii = 0
            jj = 0
            c = 0
            while ii < blen:
                while jj < blen:
                    if ii < jj:
                        c = c + ball[ii].acolb(ball[jj])
                    jj = jj + 1
                ii = ii + 1
                jj = 0

            if c == 0:
                for a in range(blen):
                    ball[a].move(t)
                v1.clear()
                v2.clear()
                mt.clear()
                break

            if c != 0:
                iii = 0
                jjj = 0
                while iii < blen:
                    while jjj < blen:
                        if iii < jjj:
                            if ball[iii].acolb(ball[jjj]) != 0:
                                mt.append(ball[iii].cotime(ball[jjj]))
                                v1.append(iii)
                                v2.append(jjj)
                        jjj = jjj + 1
                    iii = iii + 1
                    jjj = 0

                if len(mt) == 1:
                    tc = mt[0]
                if len(mt) > 1:
                    le = len(mt)
                    im = 0
                    tm = 0
                    k = 0
                    while k < le - 1:
                        while im < le - 1:
                            if mt[im] > mt[im + 1]:
                                tm = mt[im]
                                t1 = v1[im]
                                t2 = v2[im]
                                mt[im] = mt[im + 1]
                                mt[im + 1] = tm
                                v1[im] = v1[im + 1]
                                v2[im] = v2[im + 1]
                                v1[im + 1] = t1
                                v2[im + 1] = t2
                            im = im + 1
                        k = k + 1
                        im = 0
                    tc = mt[0]

                    l = 1
                    while l < len(mt):
                        if mt[l] == mt[l - 1]:
                            num = num + 1
                            l = l + 1
                        else:
                            mt[l] != mt[l - 1]
                            break
                print(tc)
                if t < tc:
                    for a in range(blen):
                        ball[a].move(t)
                    v1.clear()
                    v2.clear()
                    mt.clear()
                    break

                if t >= tc:
                    t = t - tc
                    for a in range(blen):
                        ball[a].move(tc)
                    for u in range(num):
                        ball[v1[u]].coll(ball[v2[u]])
                    v1.clear()
                    v2.clear()
                    mt.clear()

        print(time[i])
        for m in range(len(ball)):
            ball[m].pri()

        i = i + 1


if __name__ == "__main__":
    main()
