#!/usr/bin/env python3

from collections import deque


n, q = map(int, input().split())
d = dict() # d[ぼーる番号]=index
dq = deque(range(1, n+1))
for i in range(n):
    d[i+1] = i

for _ in range(q):
    x = int(input())
    xi = d[x]
    if xi == n-1:
        l = dq[n-2]
        dq[n-2], dq[n-1] = x, l
        d[x], d[l] = d[l], d[x]
    else:
        r = dq[xi+1]
        dq[xi], dq[xi+1] = r, x
        d[x], d[r] = d[r], d[x]


ans = [0]*n
for i in range(1, n+1):
    ans[d[i]] = i
print(*ans)