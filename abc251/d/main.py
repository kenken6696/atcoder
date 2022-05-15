#!/usr/bin/env python3

w = int(input())
wl = []
for i in range(1, 101):
    wl.append(i)
    wl.append(i*100)
    wl.append(i*10000)
print(len(wl))
print(*wl)