#!/usr/bin/env python3

n = int(input())
mod = 10**9+7
# dp[n]を既存の数列に任意の数を右端に追加して作成するとみなすと､
# dp[n]=dp[n-3] + dp[n-4]...+dp[3]とおけ､dp[n-1]=dp[n-4]...を代入すると､
# dp[n]=dp[n-3] + dp[n-1]と整理できる
dp = [0]*(n+1) # 0埋めしてiterじゃなくする
dp[3:6] = 1, 1, 1
for i in range(6, n+1):
    dp[i] = dp[i-1]+dp[i-3]
print(dp[n]%mod)