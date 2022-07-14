#!/usr/bin/env python3
from collections import defaultdict
n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
M = defaultdict(int)
for i,a in enumerate(A):
    M[i+1]=a
for l in L:
    if M[l] == n:
        continue
    if M[l]+1==M[l+1]:
        continue
    else:
        M[l]+=1
ans = [0]*k
for i in range(k):
    ans[i]=M[i+1]
print(*ans)