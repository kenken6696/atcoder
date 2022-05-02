#!/usr/bin/env python3

from math import gcd

n = int(input())
A = list(map(int, input().split()))
INF = 10**6+10

# 高速素因数分解 O(nlogn)
# 素因数分解(試し割り)O(√N)で間に合わないNの時､
# 予め各数の最小素因数を調べておき､それを元に因数分解していく
D = [0]*INF # D[i]=iの最小素因数
for i in range(2, INF):
    if D[i] != 0: # Dが更新されていたら､何かしらの倍数であり､最小素因数たり得ない
        continue
    for k in range(1, INF): # D[iの倍数]更新
        if i*k < INF:
            if D[i*k] == 0:
                D[i*k] = i
        else:
            break
def fast_prime_factorize(x):
    prime = []
    while 1 < x:
        prime.append(D[x])
        x //= D[x]
    return prime

pairwise = True
prime_used = [False]*INF
for i in range(n):
    prime_s = set(fast_prime_factorize(A[i]))
    for j in prime_s:
        if prime_used[j]:
            pairwise=False
            break
        else:
            prime_used[j]=True
if pairwise:
    print("pairwise coprime")
    exit()

g = A[0]
for i in range(1, n):
    g = gcd(g, A[i])
if g == 1:
    print("setwise coprime")
else:
    print("not coprime")

