#!/usr/bin/env python3
n = int(input())
nl = [ i for i in range(2, 2*n+2) ]
print(1)
while True:
    t = int(input())
    if t != 0:
        nl.remove(t)
        a = nl[0]
        nl.remove(a)
        print(a)
    else:
        exit()