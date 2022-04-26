#!/usr/bin/env python3

from collections import defaultdict

n, k = map(int, input().split())
c_l = [ list(map(int, input().split())) for _ in range(n) ]
c_l = sorted(c_l, key=lambda x: x[0])
m = k
for i in range(n):
    if i == 0:
        now_c = c_l[i][0]
        if m < now_c:
            print(m)
            exit()
        else:
            m = m - now_c + c_l[i][1]
    else:
        now_c = c_l[i][0] - c_l[i-1][0]
        if m >= now_c:
            m = m - now_c + c_l[i][1]
        else:
            print(c_l[i-1][0]+m)
            exit()
print(c_l[-1][0]+m)