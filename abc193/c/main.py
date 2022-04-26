#!/usr/bin/env python3

n = int(input())
canset = set()

for i in range(2, 10**5+10):
    for j in range(2, 1000):
        if i**j <= n:
            canset.add(i**j)
        else:
            break

print(n-len(canset))