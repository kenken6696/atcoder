#!/usr/bin/env python3

s = input()
ans = [] # store local variables

def dfs(i, n, ns):
    if i == 3:
        if n == 7:
            ans.append(ns + '=7')
            return 
        else:
            return

    dfs(i+1, n + int(s[i+1]), ns + '+' + s[i+1])
    dfs(i+1, n - int(s[i+1]), ns + '-' + s[i+1]) 


dfs(0, int(s[0]), s[0])
print(ans[0])