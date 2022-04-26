#!/usr/bin/env python3

from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
ans =  0
dl = []
d = defaultdict(list) #  [Aの値] = iter

def make_divisors(n): # 約数列挙 O(√N)
    # 15--1/15,3/5のようにlower/upperのペアごとに管理していく
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1] # upperは逆順して昇順にする

for i in range(n):
    d[A[i]].append(i)
    l= make_divisors(A[i])
    dl.append([l, l[::-1]]) # lower [1,3,9], upper[9,3,1]

for li, ui in dl:
    for i in range(len(li)):
        llen, ulen = len(d[li[i]]), len(d[ui[i]])
        ans += llen * ulen
print(ans)