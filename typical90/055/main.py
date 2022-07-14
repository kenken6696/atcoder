#!/usr/bin/env python3

from collections import defaultdict


n, p, q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for ai in range(n-4):
    for bi in range(ai+1, n-3):
        for ci in range(bi+1, n-2):
            for di in range(ci+1, n-1):
                for ei in range(di+1, n):
                    #r = ((((((A[ai]*A[bi]%p)*A[ci])%p)*A[di])%p)*A[ei])%p
                    r = ((((A[ai]%p)*(A[bi]%p)%p))*((A[ci]%p)*(A[di]%p)%p)%p)*(A[ei]%p)%p
                    if r==q:
                        ans += 1

print(ans)