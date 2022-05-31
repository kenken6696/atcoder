#!/usr/bin/env python3

a, b, c = map(int, input().split())
if a <= b and b <= c:
    print("Yes")
elif a >= b and b >= c:
    print("Yes")
else:
    print("No")