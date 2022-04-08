n = int(input())
A = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = max(dp[i], dp[i]+A[i])
print(dp[n])