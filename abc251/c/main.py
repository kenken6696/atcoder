#!/usr/bin/env python3

from collections import defaultdict


n = int(input())
ori_d = defaultdict(lambda:-2)
max_p, max_i = 0, 0
S = [ list(input().split()) for _ in range(n) ]
for i, si in enumerate(S):
    s, t = si
    t = int(t)
    if ori_d[s] == -2:
        # 現時点でオリジナル
        ori_d[s] = 1
        if max_p < t:
            max_p  = t
            max_i = i
        elif max_p == t:
            max_i = min(max_i, i)
print(max_i+1)