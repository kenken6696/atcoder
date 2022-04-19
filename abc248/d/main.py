#!/usr/bin/env python3

from bisect import bisect_left
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
q = int(input())
Q = [ list(map(int, input().split())) for _ in range(q) ]

d = defaultdict(list) # d[x] = xであるAのindex
for i in range(n):
    d[A[i]].append(i)

for i in range(q):
    l, r, x = Q[i]
    min_i = bisect_left(d[x], l-1)
    max_i = bisect_left(d[x], r)
    print(max_i-min_i)