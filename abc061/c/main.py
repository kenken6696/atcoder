#!/usr/bin/env python3

from collections import defaultdict


n, k = map(int, input().split())
d = defaultdict(int) # d[a]=sum(b)
for i in range(n):
    a, b = map(int, input().split())
    d[a] += b
d = sorted(d.items(), key=lambda x:x[0]) # keyでソートして､小さい順にチェックする
ans = 0
for a,b in d:
    k -= b
    if k <= 0:
        ans = a
        print(ans)
        exit()
ans = a
print(ans)

