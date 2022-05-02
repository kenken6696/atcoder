#!/usr/bin/env python3


n, w = map(int, input().split())
S = [[0,0]]+[ list(map(int, input().split())) for _ in range(n) ]
dp = [[0]*(n+1) for _ in range(w+1)] # dp[w][i]=iまでのitemを考慮したmax_v 敢えて0を残す
for i in range(1, w+1):
    max_v = 0
    for j in range(1, n+1):
        wj, vj = S[j]
        if i >= wj:
            dp[i][j] = max(dp[i][j-1], dp[i-wj][j-1]+vj)
        else:
            dp[i][j] = dp[i][j-1]
print(dp[w][n])