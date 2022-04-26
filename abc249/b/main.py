#!/usr/bin/env python3

n = list(input())
s_n = set(n)
in_low = False
in_up = False
for i in n:
    if i.islower():
        in_low=True
    else:
        in_up=True
    if in_low and in_up:
        break

if in_low and in_up and len(n) == len(s_n):
    print('Yes')
else:
    print('No')