#!/usr/bin/env python3

import itertools


n, w = map(int, input().split())
A = list(map(int, input().split()))
ans_s = set()
for a in A:
    if a <= w:
        ans_s.add(a)
if n >= 2:
    cmbs_two = itertools.combinations(range(n), 2) #組み合わせ重複なし
    for cmb in cmbs_two:
        num = 0
        for i in cmb:
            num += A[i]
        if num <= w:
            ans_s.add(num)
if n >= 3:
    cmbs_three = itertools.combinations(range(n), 3) #組み合わせ重複なし
    for cmb in cmbs_three:
        num = 0
        for i in cmb:
            num += A[i]
        if num <= w:
            ans_s.add(num)
print(len(ans_s))
