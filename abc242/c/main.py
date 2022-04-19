#!/usr/bin/env python3

n = int(input())
mod = 998244353
ans = 0
if n == 1:
    ans = 9
elif n < 9:
    # 1,9なし､どっちか のみ
    without_edges = 7*3**(n-1)
    with_edge = 0
    for i in range(1, n):
        with_edge += 2**i * 3**(n-1-i)
    ans = without_edges + with_edge*2
else:
    # 1,9なし､どっちか､どっちも
    without_edges = 7*3**(n-1)
    with_edge = 0
    with_edges = 0
    for i in range(1, n):
        with_edge += 2**i * 3**((n-1-i)+(n-9-i))
        if i > n-9:
            with_edges += 2**i * 3**(n-1-i)
    ans = without_edges + with_edge*2 + with_edges

print(ans%mod)