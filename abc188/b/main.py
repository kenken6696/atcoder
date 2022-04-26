#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += A[i]*B[i]
if ans == 0:
    print('Yes')
else:
    print('No')