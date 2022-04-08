#!/usr/bin/env python3
from decimal import getcontext
import math
from fractions import Fraction

getcontext().prec = 9
n, k = map(Fraction, input().split())
win_per = 0

for i in range(1,int(n)+1):
    if i <= k:
        x = Fraction(math.ceil(math.log2(k/i)))
        win_per += (Fraction('1')/n) * (Fraction('1')/Fraction('2')) ** x
    else:
        win_per += (Fraction('1')/n)

print('{:.9f}'.format(float(win_per)))

# 今回は､Fraction使う必要なかったみたいだが､正確な計算をするためにはFraction