#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(n):
    if i == 0 and A[i] != 0:
        # 最初が0じゃないなら､0
        print(0)
        break

    if i == n-1:
        # 最初が0で､間も空いてない
        if A[n-1] == 0:
            print(1)
        else:
            print(A[n-1]+1)
        break

    if A[i+1] - A[i] >= 2:
        # 最初が0で､間開いてるなら
        print(A[i]+1)
        break
