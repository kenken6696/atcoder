#!/usr/bin/env python3

s = input().replace(' ', '')
t = input().replace(' ', '')

A = ['RGB', 'GBR', 'BRG']
B = ['RBG', 'GRB', 'BGR']

if (s in A) and (t in A):
    print('Yes')
elif (s in B) and (t in B):
    print('Yes')
else:
    print('No')