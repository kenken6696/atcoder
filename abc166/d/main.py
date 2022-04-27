#!/usr/bin/env python3

x = int(input())
ans = []
for a in reversed(range(-10**3, 10**3)):
    for b in range(-10**3, a):
        if a**5 - b**5 == x:
            print(a,b)
            exit()