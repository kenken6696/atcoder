#!/usr/bin/env python3

N =int(input())
A=list(map(int, input().split()))

ans=-10**15
for l in range(N):
    A_min=A[l]
    for r in range(l,N):
        A_min=min(A_min,A[r])
        ans=max(ans,A_min*(r-l+1))

print(ans)