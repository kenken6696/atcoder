#!/usr/bin/env python3

n= int(input())
mod = 10**9+7
p = 1
for i in range(n):
    ai = list(map(int, input().split()))
    p *= sum(ai)%mod
print(p%mod)

