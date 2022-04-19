#!/usr/bin/env python3
from itertools import groupby

n, x, y = map(int, input().split())
A = list(map(int, input().split()))

B = [] # x-yのみの部分列list
temp = []
for i in range(n):
    if y <= A[i] <= x:
        temp.append(A[i])
    else:
        if len(temp) > 0:
            B.append(temp)
            temp = []
    if i == n-1:
        B.append(temp)

pred = lambda a: y <= a <= x  # この2行で分割しています。本質的な部分ではないので短い書き方にしましたが
B = [list(g) for key, g in groupby(A, key=pred) if key]
ans = 0

for b in B: # 部分列list
    lenb = len(b)
    x_cnt, y_cnt, e = 0, 0, 0
    for s in range(lenb):
        # start-endループでは､endが都度更新されるため尺取法できない
        # そのため､endはwhileで維持するよう尺取法をする
        while e < lenb and x_cnt * y_cnt == 0:
            # 条件満たすeを探す
            num = b[e]
            if num == x: x_cnt += 1
            if num == y: y_cnt += 1 # x,y同値対策としてelifにしない
            e += 1
        if x_cnt * y_cnt >= 1:
            # 一度見つかれば､eは伸ばしても条件満たす
            # x,y同値なら一文字でも条件満たす
             ans += lenb - (e-1) # lenb = len(b[s:])-s

        # 左側は調べ終わったので右側を1つ進める
        num = b[s]
        if num == x: x_cnt -= 1
        if num == y: y_cnt -= 1

print(ans)
