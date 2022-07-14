#!/usr/bin/env python3

n = int(input())
names = set()
ans = []
for i in range(n):
    s = input()
    if s in names:
        pass
    else:
        names.add(s)
        ans.append(i+1)
for a in ans:
    print(a)
