#!/usr/bin/env python3

n = int(input())
H = list(map(int, input().split()))
dp = [0]+[10**6]*(n-1)
dp[1] = dp[0]+abs(H[1]-H[0])
for i in range(n-2):
    dp[i+2] = min(dp[i]+abs(H[i]-H[i+2]), dp[i+1]+abs(H[i+1]-H[i+2]))
print(dp[n-1])
