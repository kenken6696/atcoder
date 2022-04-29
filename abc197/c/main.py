#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
ans = 10**10
for i in range(1<<n): # ○の隙間に|を並べる方法
    temp = A[0]
    anstemp = 0
    for shift in range(n-1): # 隙間に|を入れるか調べる
        if i >> shift & 1 == 1: # 入れる
            anstemp = temp if anstemp == 0 else anstemp^temp
            temp = A[shift+1]
        else: # 入れない
            temp = temp | A[shift+1]
    anstemp = anstemp^temp
    ans = min(ans, anstemp)
print(ans)