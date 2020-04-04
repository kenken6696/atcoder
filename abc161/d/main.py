#!/usr/bin/env python3

k = int(input())
lnln = [ i for i in range(1, 13) ]

def next_lnln(n):
    n_list = list(map(int, str(n)))
    d = n_list[len(n_list)-1] - n_list[len(n_list)-2]
    if d == -1 or d == 0:
        n_list[len(n_list)-1] += 1
    elif d == 1:
        n_list[len(n_list)-1] = n_list[len(n_list)-2]
        n_list[len(n_list)-2] += 1
 

if k > 13:
    for _ in range(k-13):
        lnln.append(next_lnln(lnln[-1]))

print(lnln[k-1])