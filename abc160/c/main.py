#!/usr/bin/env python3

k, n = map(int, input().split())
A = list(map(int, input().split()))


longest_dist = (k - A[n-1]) + A[0]

for i in range(n-1):
    if longest_dist < A[i+1] - A[i]:
        longest_dist = A[i+1] - A[i]

print(k-longest_dist)
