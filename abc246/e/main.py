#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = list()
for _ in range(n):
    S.append(list(input().split()))
x = abs(A[0]-B[0])
y = abs(A[1]-B[1])
ans = 0
if sum(A)%2 != sum(B)%2 or x < y:
    print(-1)
    exit()

for i in range(x,n+1):

    break

def check_y(A,B):
