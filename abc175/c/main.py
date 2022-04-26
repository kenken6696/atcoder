#!/usr/bin/env python3

x,k,d = map(int, input().split())
x = abs(x)
q, r = divmod(x, d)
ans = 0
if k < q:
    ans = x - d*k
else:
    if (k-q) % 2 == 0:
        ans = r
    else:
        ans = d - r
print(ans)