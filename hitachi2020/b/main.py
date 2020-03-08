#!/usr/bin/env python3

a_size, b_size, m_size = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = []
for i in range(m_size):
    m.append(list(map(int, input().split())))

# それぞれの最安値で買う
min_sum = min(a) + min(b)

# 割引使って買う
for i in range(m_size):
    s = a[m[i][0]-1] + b[m[i][1]-1] - m[i][2]
    if min_sum > s:
        min_sum = s

print(min_sum)