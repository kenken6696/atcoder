#!/usr/bin/env python3

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = 0

for i in range(n):
    if i == 0:
        X=set([A[0], B[0]])
        continue
    new_x = set()
    
    for x in X:
        if abs(A[i] - x) <= k:
            new_x.add(A[i])
        if abs(B[i] - x) <= k:
            new_x.add(B[i])
    if len(new_x)==0:
        print('No')
        exit()

    X = new_x

print("Yes")