#!/usr/bin/env python3

n, x = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]
dp = [[False]*(x+1) for _ in range(n+1)] # dp[ジャンプ回数(not_iter)][座標]
dp[0][0] = True

# 前からdp埋めていく; 逆順だとO(2^n)(n<100)となりTLE
def dfs(n, x):
    for i in range(n):
        a = S[i][0]
        b = S[i][1]
        for j in range(x+1):
            if dp[i][j]:
                if j+a <= x: dp[i+1][j+a] = True
                if j+b <= x: dp[i+1][j+b] = True
    return dp[n][x]

if dfs(n, x): print('Yes')
else: print('No')