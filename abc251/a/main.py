#!/usr/bin/env python3

n = input()

while len(n) < 6:
    n = n + n

print(n[:6])