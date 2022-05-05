#!/usr/bin/env python3

n, x = map(int, input().split())
x = list(bin(x)) #完全二分木は2進数の桁操作で表現できる
S = list(input())
for s in S:
    if s == 'L':
        x.append('0')
    elif s == 'R':
        x.append('1')
    else:
        x.pop()
print(int(''.join(x), 2))