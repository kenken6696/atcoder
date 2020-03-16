#!/usr/bin/env python3

num = int(input())
alf = ['a','b','c','d','e','f','g','h','i','j','k']
def dfs(s, mx_idx):
    if len(s) == num:
        print(s)
        return
    for i in range(mx_idx+1):
        if i == mx_idx:
            dfs(s+alf[i], mx_idx+1)
        else:
            dfs(s+alf[i], mx_idx)

dfs('', 0)