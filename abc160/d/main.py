#!/usr/bin/env python3

n, x, y = map(int, input().split())

for d in range(1, n):
    ans = 0

    if (y-1) > d:
        ans += (y-1) -d
    
    if (n-x) > d:
        ans += (n-x) -d
    
    if ((n-1) - (y-x-1)) >= d:
        ans += ((n-1) - (y-x-1)) -d+1

    print(ans)