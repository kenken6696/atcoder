#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
score  = 0
for i in range(n):
    score += abs(A[i]-B[i])
print(score)