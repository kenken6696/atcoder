#!/usr/bin/env python3
import bisect

n = int(input())
A = list(map(int, input().split()))
P,Q = [0]*n , [0]*n

def lis_from_start(m):
    '''
    mは添字
    '''
    ascending_dp = [300000]*n
    for i in range(m+1):
        ascending_dp_i = bisect.bisect(ascending_dp, A[i]-1) # 最長増加部分列(同数ng)
        ascending_dp[ascending_dp_i] = A[i]
        P[i] = max(ascending_dp_i + 1, P[i-1])
    ascending_dp_size = bisect.bisect(ascending_dp, 300000-1)
    return ascending_dp_size

def lis_from_end(m):
    '''
    mは添字
    '''
    ascending_dp = [300000]*n
    for i in reversed(range(m+1)):
        ascending_dp_i = bisect.bisect(ascending_dp, A[i]-1) # 最長増加部分列(同数ng)
        ascending_dp[ascending_dp_i] = A[i]
        if i != n-1:
            Q[i] = max(ascending_dp_i + 1, Q[i+1])
        else:
            Q[i] = ascending_dp_i + 1
    ascending_dp_size = bisect.bisect(ascending_dp, 300000-1)
    return ascending_dp_size

lis_from_start(n-1)
lis_from_end(n-1)

max_m = 0
for i in range(n):
    tmp_m = P[i] + Q[i] - 1
    max_m = max(max_m, tmp_m)

print(max_m)
