#!/usr/bin/env python3

from collections import defaultdict
from itertools import combinations


n, k = map(int, input().split())
S = [ input() for _ in range(n) ]
ans = 0
for i in range(k, n+1):
    cmbs = combinations([ ii for ii in range(n)], i) #組み合わせ重複なし
    for cmb in cmbs:
        d=defaultdict(int)
        for j in cmb: # [1,2,5]
            for s in S[j]: # abi
                d[s] += 1
        tmp_ans = 0
        for v in d.values():
            if v == k:
                tmp_ans += 1
        ans = max(ans, tmp_ans)
print(ans)