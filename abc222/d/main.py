#!/usr/bin/env python3

n, w = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

dp = []
for i in range(n+1):
    dp.append([0] * (w+1))

for i in range(n):
    for j in range(w+1):
        if A[i][0]<= j:
            dp[i+1][j] = max(dp[i][j], dp[i][j- A[i][0]] + A[i][1])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][w])