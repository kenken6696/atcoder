#!/usr/bin/env python3

def make_divisors(n):
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

n = int(input())
print(make_divisors(n))
