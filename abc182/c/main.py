#!/usr/bin/env python3

n = int(input())
lenn = len(str(n))
n_sum = 0
one_cnt = 0
two_cnt = 0
for ni in str(n):
    ni = int(ni)
    n_sum += ni
    if ni in (1,4,7):
        one_cnt+=1
    elif ni in (2,5,8):
        two_cnt+=1

r = n_sum % 3
ans = -1
if r == 0: ans = 0
elif lenn == 1: pass
elif r == 1:
    if one_cnt >= 1: ans = 1
    elif lenn >= 3 and two_cnt >= 2: ans = 2
elif r == 2:
    if two_cnt >= 1: ans = 1
    elif lenn >= 3 and one_cnt >= 2: ans = 2
print(ans)