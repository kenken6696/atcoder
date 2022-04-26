#!/usr/bin/env python3

n = int(input())
S = list(map(int, input().split()))
mod = 10**9+7
sum_s = S[-1]
ans = 0
for i in reversed(range(n-1)):
    ans += S[i] * sum_s
    sum_s += S[i]
print(ans%mod)
