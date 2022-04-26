#!/usr/bin/env python3

from itertools import combinations, combinations_with_replacement


h, w, k = map(int, input().split())
S = [ int(input()) for _ in range(h) ]

h_r = list(range(h))
w_r = list(range(w))
cmbs = combinations_with_replacement()