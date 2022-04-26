#!/usr/bin/env python3

import itertools


n, k = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]
ans = 0
pmts = itertools.permutations(range(n), n) # 順列重複なし
for pmt in pmts:
    if pmt[0] != 0:
        continue
    t = 0
    for i in range(n-1):
        t += S[pmt[i]][pmt[i+1]]
        if t > k:
            break
    t += S[pmt[-1]][0]
    if t == k:
        ans += 1

print(ans)