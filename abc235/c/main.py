#!/usr/bin/env python3

from collections import defaultdict


n, q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list) # d[a] = [ai1, ai2...]
for i in range(n):
    d[A[i]].append(i)
for _ in range(q):
    x, k = map(int, input().split())
    ans = -1
    if len(d[x])>=k:
        ans = d[x][k-1]+1 # indexなので+1
    print(ans)