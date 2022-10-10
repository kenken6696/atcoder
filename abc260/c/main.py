#!/usr/bin/env python3

import sys


n, x, y = map(int, input().split())
sys.setrecursionlimit(67108864)
def red(n):
    if n == 2:
        return (2, x*y)
    r = red(n-1)
    b = blue(n)
    return (r[0]+b[0]*x, r[1]+b[1]*x)
def blue(n):
    if n == 2:
        return (1, y)
    r = red(n-1)
    b = blue(n-1)
    return (r[0]+b[0]*y, r[1]+b[1]*y)
if n==1:
    print(0)
    exit()
(r, b) = red(n)
print(b)
