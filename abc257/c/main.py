#!/usr/bin/env python3

from collections import defaultdict, deque
import heapq


n = int(input())
S = list(map(int, list(input())))
W = list(map(int, input().split()))
A, C = deque(), deque()
ans = 0

for i in range(n):
    w = W[i]
    if S[i]==1:
        A.append(w)
    else:
        C.append(-1*w)
A, C = list(A), list(C)
heapq.heapify(A)
heapq.heapify(C)

if len(A)==0 or len(C)==0:
    print(n)
    exit()

a_min = heapq.heappop(A)
c_max = heapq.heappop(C)*-1
if c_max < a_min:
    ans = n
elif c_max == a_min:
    ans = n-1
else:
    under_a, upper_c = 1, 1
    a_now_min = heapq.heappop(A)
    c_now_max = heapq.heappop(C)*-1
    while a_now_min <= c_max:
        under_a += 1
        if len(A)>0:
            a_now_min = heapq.heappop(A)
        else:
            break
    while c_now_max >= a_min:
        upper_c += 1
        if len(C)>0:
            c_now_max = heapq.heappop(C)*-1
        else:
            break
    ans = n - min(upper_c, under_a)
print(ans)