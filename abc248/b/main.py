#!/usr/bin/env python3

a, b, k = map(int, input().split())
ans = 0
for i in range(10**9):
    if a*k**i >=b:
        ans = i
        break
print(ans)