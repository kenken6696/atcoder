#!/usr/bin/env python3

n, k, x = map(int, input().split())
A = list(map(int, input().split()))
sum_yen = 0

for i in range(n):
    if k == 0:
        sum_yen += sum(A[i:])
        break
    used = min(k, A[i]//x)
    paid = A[i] - used * x
    sum_yen += paid
    A[i] = paid
    k -= used

if k > 0:
    A.sort(reverse=True)
    sum_yen -= sum(A[:k])

print(sum_yen)