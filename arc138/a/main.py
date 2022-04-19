#!/usr/bin/env python3

from aifc import Aifc_read


n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = n
INF = float('inf')

''' for i in reversed(range(k)):
    for j in range(k, i+ans):
        if j >= n:
            break
        if A[i] < A[j]:
            if ans>j-i:
                ans = j-i
            break
    if k-i >= ans:
        break
if ans == n:
    ans = -1 '''

left=[]
for i in range(k):
    left.append(A[i]+k-1-i)
left_choice_index=left.index(min(left))
right=[]
for i in range(k, n):
    if A[i] > A[left_choice_index]:
        right.append(A[i]+i-k)
    else:
        right.append(INF)
right_choice_index=(k)+right.index(min(right))
if A[right_choice_index]-A[left_choice_index] > 0:
    ans = right_choice_index-left_choice_index
else:
    ans = -1
print(ans)
