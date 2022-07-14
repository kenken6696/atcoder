#!/usr/bin/env python3

from collections import defaultdict


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A_mod = defaultdict(int)
B_mod = defaultdict(int)
C_mod = defaultdict(int)
ans = 0

for i in range(n):
    A_mod[A[i]%46] += 1
    B_mod[B[i]%46] += 1
    C_mod[C[i]%46] += 1

for ak, ac in A_mod.items():
    for bk, bc in B_mod.items():
        if ak+bk > 46:
            ans += ac*bc*(C_mod[46*2-ak-bk])
        elif ak+bk == 0:
            ans += ac*bc*(C_mod[0])
        else:
            ans += ac*bc*(C_mod[46-ak-bk])

print(ans)