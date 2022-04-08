#!/usr/bin/env python3

input = list(map(int, input().split()))

t = input[0]*60 + input[1]
a = input[2]*60 + input[3]

if t <= a:
    print("Takahashi")
else:
    print("Aoki")