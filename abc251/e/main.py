#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
inf = 10**10
# dp[i][0]=条件を満たす0-iまでの餌やりのうち､A[i]の餌やりをしない時の費用最小値､dp[i][1]=はA[i]ありの時
dp = [[0]*2 for _ in range(n)]
# dp[0]のとき､餌やるかやらないかを固定して､それぞれの最小値を考える
ans_with_a1, ans_without_a1 = [inf]*2

# a1ありの場合
dp[0][0], dp[0][1] = inf, A[0]
for i in range(1, n):
    dp[i][0] = dp[i-1][1] # i-1で既に餌やり済
    dp[i][1] = min(dp[i-1])+A[i] # どうせ餌やるので小さい方でよい
ans_with_a1 = min(dp[-1]) # a1で既に1に餌やり済みなので,anは考慮不要

# a1なしの場合
dp[0][0], dp[0][1] = 0, inf
for i in range(1, n):
    dp[i][0] = dp[i-1][1] # i-1で既に餌やり済
    dp[i][1] = min(dp[i-1])+A[i] # どうせ餌やるので小さい方でよい
ans_without_a1 = dp[-1][1] # a1なし､つまり1に餌必要なので,anは必要

print(min(ans_with_a1, ans_without_a1))