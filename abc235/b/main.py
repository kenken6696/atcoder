#!/usr/bin/env python3

n = int(input())
H = list(map(int, input().split()))
for i in range(n-1):
    if H[i] >= H[i+1]:
        print(H[i])
        exit()
print(H[-1])