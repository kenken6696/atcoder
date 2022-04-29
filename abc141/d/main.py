#!/usr/bin/env python3

import heapq


n, m = map(int, input().split())
S = list(map(int, input().split()))
S = list(map(lambda x: x*-1, S))
heapq.heapify(S)

for _ in range(m):
    max = heapq.heappop(S)*-1
    max = max // 2
    heapq.heappush(S, max*-1)
print(sum(S)*-1)