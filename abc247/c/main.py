#!/usr/bin/env python3

n = int(input())
def dfs(n):
    if n == 1:
        return [1]
    sn = dfs(n-1)
    return sn + [n] + sn
ans = dfs(n)
print(*ans)