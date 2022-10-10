#!/usr/bin/env python3

from collections import defaultdict


n, m, t = map(int, input().split())
A = list(map(int, input().split()))
br = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    br[x] = y
for i, a in enumerate(A): 
    t -= a
    if t <=0:
        print('No')
        exit()
    t += br[i+2]

print('Yes')