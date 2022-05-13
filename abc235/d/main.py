#!/usr/bin/env python3

from collections import defaultdict, deque

a, n = map(int, input().split())
x = 1
cnt = 0
x_s = set([x])
l = deque([(cnt, x)])
d = defaultdict(list)
cnt = 0
ans = 10**10
while l:
    cnt, x = l.popleft()
    cnt += 1

    x1 = x*a
    if x1 == n:
        ans = min(ans, cnt)
    elif cnt < ans and len(str(x1))<=len(str(n)) and x1 not in x_s:
        x_s.add(x1)
        l.append((cnt, x1))


    if x>10 and x%10 != 0:
        x2 = int(str(x)[-1]+str(x)[:-1])
        if x2 == n:
            ans = min(ans, cnt)
        elif cnt < ans and len(str(x2))<=len(str(n)) and x2 not in x_s:
            x_s.add(x2)
            l.append((cnt, x2))
if ans == 10**10:
    print(-1)
else: print(ans)