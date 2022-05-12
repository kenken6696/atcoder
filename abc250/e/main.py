#!/usr/bin/env python3
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ad = defaultdict(int) # d[i]={L[:i+1]の3乗の総和}
bd = defaultdict(int)
tempa, tempb = set(), set()
for i in range(n):
    if A[i] in tempa:
        ad[i] = ad[i-1]
    else:
        tempa.add(A[i])
        ad[i] = ad[i-1] + (A[i]**3)
    if B[i] in tempb:
        bd[i] = bd[i-1]
    else:
        tempb.add(B[i])
        bd[i] = bd[i-1] + (B[i]**3)

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    ans = "Yes" if ad[x-1]==bd[y-1] else "No"
    print(ans)