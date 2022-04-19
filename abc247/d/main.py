#!/usr/bin/env python3

import collections

n = int(input())
S = [ list(map(int, input().split())) for _ in range(n) ]

d = collections.deque()
for i in range(n):
    if S[i][0] == 1:
            d.append((S[i][1],S[i][2])) # x, c
    elif S[i][0] == 2:
        need_c = S[i][1]
        ans = 0
        while need_c > 0:
            b = d.popleft()
            x, c = b
            if c < need_c:
                ans += x*c
                need_c -= c
            elif c > need_c:
                ans += x*need_c
                print(ans)
                c -= need_c
                d.appendleft((x, c))
                need_c = 0
            else:
                ans += x*c
                print(ans)
                need_c = 0