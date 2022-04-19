#!/usr/bin/env python3

from collections import defaultdict

n = int(input())
XY = [ list(map(int, input().split())) for _ in range(n) ]
S = input()
INF = 10**9+1 # 累乗計算は10^7で2sなので累乗もNG!
right_min, left_max = defaultdict(lambda:INF), defaultdict(lambda:-INF) # iの左端とjの右端

ans = 'No'
for i in range(n): # O(n)
    x, y = XY[i][0], XY[i][1]
    # 各iで少なくとも1回衝突が起こることを確認するには､一番右にいるLの人<一番左にいるRの人､であればよい
    if S[i] == 'L': left_max[y] = max(x, left_max[y])
    else: right_min[y] = min(x, right_min[y])
for y in left_max.keys(): # O(1)
    if right_min[y] < left_max[y]: # dict.slice avg O(1) max O(k)
        ans = 'Yes'
        break
print(ans) # total O(n)