#!/usr/bin/env python3

from math import cos, pi, sin

n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())
xcntr, ycntr = (x0+xn2)/2, (y0+yn2)/2

x0 -= xcntr
y0 -= ycntr

x1 = cos(2*pi/n)*x0 - sin(2*pi/n)*y0
y1 = sin(2*pi/n)*x0 + cos(2*pi/n)*y0

x1 += xcntr
y1 += ycntr

print(x1, y1)