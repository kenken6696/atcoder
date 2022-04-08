#!/usr/bin/env python3

n, p = map(int, input().split())
A = list(map(int, input().split()))
print(len(list(filter(lambda x: x < p, A))))
