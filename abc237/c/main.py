#!/usr/bin/env python3
from collections import deque

d = deque(input())
can_add = True
ans = 'Yes'
while len(d) > 1:
    r = d.pop()
    if r != d[0]:
        if r == 'a':
            if can_add == False:
                ans = 'No'
                break
        else:
            ans = 'No'
            break
    else:
        d.popleft()
        if r != 'a':
            can_add = False

print(ans)
