#!/usr/bin/env python3

import math

def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)

n, a, b = map(int, input().split())
def sum(s, e, num):
    return (s+e)*num//2
all_sum = sum(1, n, n)
a_sum, b_sum, lcm_sum = 0, 0, 0
if n >= a:
    a_num = n//a
    a_sum = sum(a, a*a_num, a_num)
if n >= b:
    b_num = n//b
    b_sum = sum(b, b*b_num, b_num)
ab_lcm = lcm(a, b)
if n >= ab_lcm:
    lcm_num = n//ab_lcm
    lcm_sum = sum(ab_lcm, ab_lcm*lcm_num, lcm_num)
ans = all_sum - a_sum - b_sum + lcm_sum
print(ans)