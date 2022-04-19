#!/usr/bin/env python3
from collections import defaultdict, deque

n = int(input())
A = list(map(int, input().split()))

q = deque()
dct = defaultdict(int) # q.indexより高速
ans = 0
for a in A:
    q.append(a)
    dct[a] += 1
    while len(q) != 0 and dct[a]>1:
            rm = q.popleft()
            dct[rm] -= 1
    ans = max(ans, len(q)) # 毎回maxしてもったいない
print(ans)