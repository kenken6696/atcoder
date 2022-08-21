#!/usr/bin/env python3

x, y, n = map(int, input().split())
if x*3>y:
    q, r = divmod(n, 3)
    ans = q*y+r*x
else:
    ans = n*x
print(ans)