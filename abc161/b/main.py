#!/usr/bin/env python3

n, m = map(int, input().split())
P = sorted(list(map(int, input().split())))

lmt = sum(P) / (4*m)

if lmt <= P[-1*m]: # =付け忘れ
    print('Yes')
else:
    print('No')