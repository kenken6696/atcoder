#!/usr/bin/env python3

from collections import deque


sl = list(input())
tl = list(input())
sd = deque()
temp = [sl[0], 1]
for s in sl[1:]:
    if temp[0]==s:
        temp[1]+= 1
    else:
        sd.appendleft(temp)
        temp = [s, 1]
sd.appendleft(temp)
td = deque()
temp = [tl[0], 1]
for t in tl[1:]:
    if temp[0]==t:
        temp[1]+= 1
    else:
        td.appendleft(temp)
        temp = [t, 1]
td.appendleft(temp)


if len(sd) != len(td):
    print('No')
    exit()

ans = ''
for s, t in zip(sd, td):
    if s[0]==t[0]:
        if s[1] == t[1]:
            ans = 'Yes'
        elif s[1] >= 2 and t[1]>s[1]:
            ans = 'Yes'
        else:
            ans = 'No'
            break
    else:
        ans = 'No'
        break
print(ans)