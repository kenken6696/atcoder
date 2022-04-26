#!/usr/bin/env python3
from fractions import Fraction
x = Fraction('1')/Fraction('3')
t = int(input())
for i in range(t):
    n, a, b, x, y, z= map(int, input().split())
    ans = 0
    y_c, z_c = Fraction(y)/Fraction(a), Fraction(z)/Fraction(b)
    if x >= y_c >= z_c:
        q, r = divmod(n, b)
        n = r
        ans += q*z
        q, r = divmod(n, a)
        n = r
        ans += q*y
        ans += r*x
    elif x >= z_c >= y_c:
        q, r = divmod(n, a)
        n = r
        ans += q*y
        q, r = divmod(n, b)
        n = r
        ans += q*z
        ans += r*x
    elif y_c >= x >= z_c:
        q, r = divmod(n, b)
        n = r
        ans += q*z
        ans += r*x
    elif z_c >= x >= y_c:
        q, r = divmod(n, a)
        n = r
        ans += q*y
        ans += r*x
    else:
        ans += n*x
    print(ans)