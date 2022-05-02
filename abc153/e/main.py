#!/usr/bin/env python3

h, n = map(int, input().split())
dp = [10**10] * (h+1) # dp[hp]=min_mp
dp[0] = 0 # 0埋め
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(h):
        if i+a < h:
            dp[i+a] = min(dp[i+a], dp[i]+b)
        else:
            dp[h] = min(dp[h], dp[i]+b)

print(dp[h])