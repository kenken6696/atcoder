#!/usr/bin/env python3

from collections import deque


n = int(input())
s = input()

'''
1..nならO(n**2)だが､逆順でdequeを使えばO(n)
A = [0]
pre_i = 0
for i in range(n):
    if s[i] == 'R':
        A = A[:pre_i+1] + [i+1] + A[pre_i+1:]
        pre_i = pre_i+1
    else:
        A = A[:pre_i] + [i+1] + A[pre_i:] '''
A = deque([n])
for i in reversed(range(n)):
    if s[i] == 'R':
        A.appendleft(i)
    else:
        A.append(i)

print(*A)