#!/usr/bin/env python3

n, w = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(n+1):
    dp.append([False] * (w+1))

for i in range(n):
    for j in range(w+1):
        if A[i]<= j:
            if dp[i][j- A[i]]:
                dp[i+1][j] = dp[i][j- A[i]] + A[i]
        else:
            dp[i+1][j] = dp[i][j]

if dp[n][w]:
    print("Yes")
else:
    print("No")