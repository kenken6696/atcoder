#!/usr/bin/env python3

from collections import deque


dq = deque(input())
q_n = int(input())
Q = [ list(input().split()) for _ in range(q_n) ]
is_reversed = False

for i in range(q_n):
    q = Q[i]
    if q[0] == '1':
        is_reversed = False if is_reversed else True
    else:
        if q[1] == '1':
            if is_reversed:
                dq.append(q[2])
            else:
                dq.appendleft(q[2])
        else:
            if is_reversed:
                dq.appendleft(q[2])
            else:
                dq.append(q[2])

if is_reversed:
    print(''.join(list(dq)[::-1]))
else:
    print(''.join(dq))