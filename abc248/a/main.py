#!/usr/bin/env python3

from collections import defaultdict


n = input()
z=defaultdict(lambda:False)
for s in n:
    z[s]=True
for i in range(10):
    if z[str(i)] == False:
        print(i)
        exit()
