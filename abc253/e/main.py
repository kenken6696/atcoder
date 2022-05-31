#!/usr/bin/env python3

n, m, k = map(int, input().split())
mod = 998244353
dp = [[0]*(m+1) for _ in range(n+1)] # dp[i][Ai]=それまでの場合の数の累積和/貰うDP
for i in range(1, n+1):
    if i == 1:
        for j in range(1, m+1):
            dp[i][j] = dp[i][j-1]+1
        continue
    for j in range(1, m+1):
        if k == 0:
            dp[i][j] = (dp[i][j-1] + (dp[i-1][m]))%mod
        elif 1 <= j-k and j+k <= m:
            dp[i][j] = (dp[i][j-1] + (dp[i-1][m] - dp[i-1][j+k-1] + dp[i-1][j-k]))%mod
        elif 1 <= j-k and j+k > m:
            dp[i][j] = (dp[i][j-1] + (dp[i-1][j-k]))%mod
        elif 1 > j-k and j+k <= m:
            dp[i][j] = (dp[i][j-1] + (dp[i-1][m] - dp[i-1][j+k-1]))%mod
        else:
            dp[i][j] = dp[i][j-1]
ans = dp[-1][-1]%mod
print(ans)