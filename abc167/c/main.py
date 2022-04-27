#!/usr/bin/env python3

import itertools


n, m, x = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]
ans  = 10**10

# 解1 combinationでやる
''' iters = list(range(n))
for i in range(1, n+1):
    cmbs = itertools.combinations(iters, i) #組み合わせ重複なし
    for cmb in cmbs: # [1, 5, 8]
        sum_l = [0]*(m+1)
        for j in cmb: # 1
            for c in range(m+1):
                sum_l[c] += S[j][c]
        flg = False
        for c in sum_l[1:]:
            if c < x:
                sum_l[0] = 10**7
                break
        ans = min(ans, sum_l[0])'''

# 解2 BIT全探索
## 各参考書を買う買わないを[10100](右から左)として管理
for i in range(1<<n): # 買い方の組み合わせ 1<<nは､2**n+1と同値
    cost, skill_l = 0, [0]*m
    for shift in range(n): # 各参考書ごとに確認
        if i>>shift & 1 == 1: # i冊目を買うか(i番目が1か確認)
            cost += S[shift][0]
            for a in range(m):
                skill_l[a] += S[shift][a+1]
    if min(skill_l) >= x:
        ans = min(ans, cost)


if ans == 10**10: print(-1)
else: print(ans)