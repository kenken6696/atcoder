#!/usr/bin/env python3
import string

n, x = map(int, input().split())
abc = list(string.ascii_uppercase)

q, r = divmod(x, n)
if r > 0:
    print(abc[q])
else:
    print(abc[q-1])