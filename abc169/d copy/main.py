#!/usr/bin/env python3

import collections

n = int(input())
def prime_factorize(n): # 素因数分解 試し割り法
    # 偶数か見て､奇数分はひたすら試す
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c = collections.Counter(prime_factorize(n)) #配列情報はcounterを使う
ans = 0
for v in c.values():
    i = 1
    while v >= i:
        ans += 1
        v -= i
        i += 1

print(ans)