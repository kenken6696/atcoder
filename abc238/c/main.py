#!/usr/bin/env python3

n = int(input())
mod = 998244353
d = len(str(n))
ans = 0
for i in range(d-1):
    fi = 9*10**i
    ans += (1+fi)*fi//2

fn = n-10**(d-1)+1
ans += (1+fn)*fn//2

print(ans%mod)