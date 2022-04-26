#!/usr/bin/env python3

a, b, wkg = map(int, input().split())
wg = wkg * 1000

min_a = 10**15
max_a = -10**15

for x in range(1, 10**6+10):
    if a*x <= wg <= b*x:
        min_a = min(min_a, x)
        max_a = max(max_a, x)
if min_a == 10**15:
    print('UNSATISFIABLE')
else:
    print(min_a, max_a)