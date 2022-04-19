#!/usr/bin/env python3

from collections import deque

n, m, k = map(int, input().split())
mod = 998244353
ans = 0
dp = [[0] * (k+1) for _ in range(n+1)] # dp[n][sum]=組み合わせ数
dp[0][0] = 1
for i in range(n):
    for sum in range(k+1):
        for j in range(1, m+1):
            if sum+j <= k:
                dp[i+1][sum+j] += dp[i][sum]
for sum in range(n, k+1):
    ans += dp[n][sum]
print(ans%mod)
