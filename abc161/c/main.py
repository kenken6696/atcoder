#!/usr/bin/env python3

n, k = map(int, input().split())

#while n > abs(n-k):
#    n = abs(n-k)
while 2*n > k:
    
    if n > k:
        n = n%k
    elif n <= k:
        n = k-n

print(n)