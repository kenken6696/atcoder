#!/usr/bin/env python3

n = int(input())
t = input()
direction = [0,1,2,3]
d_i = 0
x, y = 0, 0

for s in t:
    if s == 'R':
        d_i = (d_i + 1) % 4
    elif s == 'S':
        if d_i == 0:
            x += 1
        elif d_i == 1:
            y -= 1
        elif d_i == 2:
            x -= 1
        elif d_i == 3:
            y += 1

print(x, y)