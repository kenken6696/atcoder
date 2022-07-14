#!/usr/bin/env python3

h, w = map(int, input().split())
Aij = [[0]*w for i in range(h)]
for i in range(h):
    Aij[i] = list(map(int, input().split()))

Aijt = list(zip(*Aij))
sum_w = [0]*w
for j in range(w):
    sum_w[j] = sum(Aijt[j])

for i in range(h):
    ans_i = [0]*w
    sum_i = sum(Aij[i])
    for j in range(w):
        ans_i[j] = sum_i + sum_w[j] - Aij[i][j]
    print(*ans_i)
