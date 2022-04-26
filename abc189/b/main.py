#!/usr/bin/env python3

from fractions import Fraction

n, x = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]
ans = -1
for i in range(n):
    x -= Fraction(S[i][0]) * Fraction(S[i][1]) / Fraction(100)
    if x < 0:
        ans = i+1
        break

print(ans)