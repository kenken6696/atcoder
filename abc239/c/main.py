#!/usr/bin/env python3

x1, y1, x2, y2 = map(int, input().split())
l = [(1,2), (1,-2), (2,1), (2, -1), (-1,2), (-1,-2), (-2,1), (-2, -1)]
one_infive = []
two_infive = []
for i in l:
    x_add, y_add = i
    one_infive.append((x1+x_add, y1+y_add))
    two_infive.append((x2+x_add, y2+y_add))
for i in one_infive:
    if i in two_infive:
        print('Yes')
        exit()
print('No')