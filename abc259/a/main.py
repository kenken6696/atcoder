#!/usr/bin/env python3

n, m, x, t, d = map(int, input().split())
ans = 0
if m >= x:
    ans = t
else:
    ans = t - (x-m)*d
print(ans)