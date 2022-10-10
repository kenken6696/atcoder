#!/usr/bin/env python3

from collections import defaultdict
from email.policy import default


n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_l = [0]*n
B_l = [0]*n
AB_l = [0]*n
for i in range(n):
    A_l[i] = (i+1, A[i])
    B_l[i] = (i+1, B[i])
    AB_l[i] = (i+1, A[i]+B[i])
passed = []
A_sort = sorted(A_l, reverse=True, key=lambda x: x[1])
for a in A_sort[:x]:
    passed.append(a[0])

B_sort = sorted(B_l, reverse=True, key=lambda x: x[1])
b_passed = 0
for b in B_sort:
    if b_passed < y and b[0] not in passed:
        passed.append(b[0])
        b_passed += 1

AB_sort = sorted(AB_l, reverse=True, key=lambda x: x[1])
ab_passed = 0
for ab in AB_sort:
    if ab_passed < z and ab[0] not in passed:
        passed.append(ab[0])
        ab_passed += 1

ans = sorted(passed)
print(*ans, sep='\n')
