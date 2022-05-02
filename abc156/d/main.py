#!/usr/bin/env python3
from itertools import combinations

n, a, b = map(int, input().split())
mod=10**9+7

def combination_mod(n, r, mod):
    # 分子 n*(n-1)*..*(n-r+1) %mod
    numerator=1
    for i in range(n-r+1,n+1):
        numerator=(numerator*i)%mod
    # 分母 r*(r-1)*...*1 %modの逆元%mod
    denominator=1
    for i in range(1,r+1):
        denominator=(denominator*i)%mod
    denominator_inv=pow(denominator,-1,mod)
    return numerator*denominator_inv%mod

ans = pow(2,n,mod)-1 - (combination_mod(n, a, mod)+combination_mod(n, b, mod))
print(ans%mod)
