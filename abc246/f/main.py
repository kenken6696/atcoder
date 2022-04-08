#!/usr/bin/env python3
import itertools


mod = 998244353
n, l = map(int, input().split())
S = []
for i in range(n):
    S.append(set(input()))
ans = 0

for i in range(n):
    ans += len(S[i])**l
    for j in range(i):
        itertools.combinations(S[i],S[j])
        ans -= len(S[i]&S[j])**l

print(ans%mod)