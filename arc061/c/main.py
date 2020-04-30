#!/usr/bin/env python3

s = input()

def dfs(i, t):
    if i == len(s) - 1:
        return sum(list(map(int, t.split('+'))))
    return dfs(i+1, t + s[i+1]) + dfs(i+1, t + '+' + s[i+1])

print(dfs(0, s[0]))