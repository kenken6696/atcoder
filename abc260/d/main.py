#!/usr/bin/env python3

from bisect import bisect_right, insort_left, insort_right
from collections import defaultdict
import heapq


n, k = map(int, input().split())
P = list(map(int, input().split()))
ans = [-1]*n
c = []
cl = defaultdict(list)
for i in range(1, n+1):
    now = P[i-1]
    if len(c)==0 or now >= c[-1]:
        c.append(now)
        cl[now].append(now)

        if len(cl[now]) == k:
            for d in cl[now]:
                ans[d-1] = i
            c.remove(now)
            cl.pop(now)
    else:
        idx = bisect_right(c, now)
        top = c[idx]
        cl[top].append(now)

        if len(cl[top]) == k:
            for d in cl[top]:
                ans[d-1] = i
            c.remove(top)
            cl.pop(top)

print(*ans, sep='\n')