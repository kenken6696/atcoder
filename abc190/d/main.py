#!/usr/bin/env python3
n = int(input())
ans = set()
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

div_l = make_divisors(2*n)
divm_l = []
for div in div_l:
    divm_l.append(-1*div)
for i in range(len(div_l)):
    upper = div_l[i]
    lower = div_l[-1-1*i]
    if (lower+upper-1)%2 == 0:
        end = (lower+upper-1)/2
        start = upper - end
        if start <= end:
            ans.add((start, end))

    upper = divm_l[i]
    lower = divm_l[-1-1*i]
    if (lower+upper-1)%2 == 0:
        end = (lower+upper-1)/2
        start = upper - end
        if start <= end:
            ans.add((start, end))
print(len(ans))
