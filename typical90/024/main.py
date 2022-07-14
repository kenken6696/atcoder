#!/usr/bin/env python3

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dist = 0
for i in range(n):
    dist += abs(A[i]-B[i])
if dist<=k and (dist-k)%2 == 0:
    print('Yes')
else:
    print('No')

