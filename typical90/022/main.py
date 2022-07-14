#!/usr/bin/env python3

from math import gcd


a, b, c= map(int, input().split())
g = gcd(gcd(a, b), c)
ans = (a+b+c)//g-3
print(ans)
