#!/usr/bin/env python3

n = int(input())
mod = 998244353
ans = 0
dp = [[0]*10 for _ in range(n+1)] # dp[i][j]=i桁目がjの場合の数
dp[2][1], dp[2][9] = 2, 2
dp[2][2:9] = [3]*7

for i in range(3, n+1):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1])%mod
        elif j == 9:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%mod
print(sum(dp[n])%mod)