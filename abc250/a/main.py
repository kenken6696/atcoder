#!/usr/bin/env python3

h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
if r > 1:
    if h > r:
        ans += 2
    elif h == r:
        ans += 1
elif r == 1 and h > r:
    ans += 1
if c > 1:
    if w > c:
        ans += 2
    elif w == c:
        ans += 1
elif c == 1 and w > c:
    ans += 1
print(ans)