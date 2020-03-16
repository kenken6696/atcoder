#!/usr/bin/env python3
from decimal import *

a, b, c = map(Decimal, input().split())
if a.sqrt() + b.sqrt() < c.sqrt():
    print('Yes')
else:
    print('No')