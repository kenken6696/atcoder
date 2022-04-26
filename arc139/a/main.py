#!/usr/bin/env python3

n = int(input())
T = list(map(int, input().split()))
A = [0]*n
A[0] = int('1'+'0'*T[0], 2)
B = []

def make_top(top_2):
    if top_2 == '':
        return '1'
    elif top == '0b1':
        return '11'
    top_2 = bin(int(top_2[:-1], 2) + 1)
    return top_2 + '1'

for i in range(1, n):
    base = '0'*T[i]
    if len(bin(A[i-1])) > 2+T[i]:
        top = bin(A[i-1])[:-1*(T[i]+1)]+'1'
    else: top = make_top('')
    a_2 = (top+base)
    while A[i-1] >= int(a_2, 2):
        top = make_top(top)
        a_2 = top+base
    A[i] = int(a_2, 2)
for a in A:
    B.append(bin(a))
print(A[n-1])