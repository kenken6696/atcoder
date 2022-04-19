#!/usr/bin/env python3

n, m = map(int, input().split())
S = list(input().split())
T = list(input().split())
e_i = 0

for s in S:
    if s == T[e_i]:
        print("Yes")
        e_i += 1
    else:
        print("No")