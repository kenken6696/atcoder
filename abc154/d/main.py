#!/usr/bin/env python3

import itertools

n, k = map(int, input().split())
P = list(map(int, input().split()))
E = []
for p in P:
    E.append((1+p)/2)

AC = list(itertools.accumulate(E))+[0] # [1,3,6,10,15,21,0]
ans = 0
for i in range(k-1, n):
    ans = max(ans, AC[i]-AC[i-k])
print(ans)