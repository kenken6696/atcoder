#!/usr/bin/env python3

import math


a, b = map(int, input().split())
def lcm(a, b):
    y = a*b // math.gcd(a, b)
    return int(y)
ans = lcm(a, b)
if ans > 10**18:
    print('Large')
else:
    print(ans)