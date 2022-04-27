#!/usr/bin/env python3

from collections import deque


n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ans = 0
pre_dq = deque()
for i in range(n):
    st = t[i]
    my = ''
    if i < k:
        if st == 'r': my = 'p'; ans += p
        elif st == 's': my = 'r'; ans += r
        else: my = 's'; ans += s
    else:
        pre = pre_dq.popleft()
        if st == 'r':
            if len(pre) == 2 or pre != 'p': my = 'p'; ans += p
            else: my = ['r', 's']
        elif st == 's':
            if len(pre) == 2 or pre != 'r': my = 'r'; ans += r
            else: my = ['s', 'p']
        elif st == 'p':
            if len(pre) == 2 or pre != 's': my = 's'; ans += s
            else: my = ['p', 'r']
    pre_dq.append(my)
print(ans)