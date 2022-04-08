#!/usr/bin/env python3

n, m = map(int, input().split())
l_list = []
r_list = []
for _ in range(m):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)

if min(r_list) >= max(l_list):
    ans = (min(r_list) - max(l_list) + 1)
else:
    ans = 0
print(ans)