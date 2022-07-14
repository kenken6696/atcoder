#!/usr/bin/env python3

n = int(input())
abc = list(map(int, input().split()))
a, b, c = sorted(abc) #昇順
ans = 10**6
for ci in range(10000):
    for bi in range(10000-ci):
        if n-bi*b-ci*c >= 0:
            q, r = divmod(n-bi*b-ci*c, a)
            if r == 0:
                ans = min(ans, q+bi+ci)

print(ans)