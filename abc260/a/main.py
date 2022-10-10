#!/usr/bin/env python3

from collections import Counter, defaultdict


n = list(input())
c = Counter(n)
for k, v in c.items():
    if v==1:
        print(k)
        exit()
print(-1)