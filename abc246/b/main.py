#!/usr/bin/env python3
import math
import decimal
a,b = map(decimal.Decimal, input().split())
c = decimal.Decimal(math.sqrt(a**2+b**2))
ans = [ a/c, b/c ]
print(*ans)