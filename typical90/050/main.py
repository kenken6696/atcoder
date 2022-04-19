#!/usr/bin/env python3

n, l = map(int, input().split())
mod = 10**9+7
INF = float('inf')

dp = [INF]*n #dp[i] i+1段目にたどり着く移動方法数
for i in range(n):
    if i < l-1:
        dp[i] = 1
    elif i == l-1:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-l]

print(dp[n-1]%mod)