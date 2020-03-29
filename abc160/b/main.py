#!/usr/bin/env python3

total = int(input())

a, mod = divmod(total, 500)
b = mod // 5

point = a*1000 + b*5

print(point)