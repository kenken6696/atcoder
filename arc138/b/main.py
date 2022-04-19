#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

def dfs(n, l):
    if n == 1:
        if l == [0]:
            return True
        else:
            return False
    if l[-1] == 0:
        if dfs(n-1, l[:-1]):
            return True
    if l[0] == 0:
        nl = []
        for i in l[1:]:
            if i==0:
                nl.append(1)
            else:
                nl.append(0)
        if dfs(n-1, nl):
            return True
    return False

if dfs(n, A):
    print("Yes")
else:
    print("No")