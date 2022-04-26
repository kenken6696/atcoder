#!/usr/bin/env python3

a, b, c, d, e, f, x = map(int, input().split())
def dis(a, b, c, x):
    d = 0
    q, r = divmod(x, (a+c))
    if r >= a:
        d = b * ((q+1)*a)
    else:
        d = b * (q*a+r)
    return d

t_d = dis(a, b, c, x)
a_d = dis(d, e, f, x)
if t_d > a_d:
    print('Takahashi')
elif t_d == a_d:
    print('Draw')
else:
    print('Aoki')