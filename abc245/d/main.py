#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [0]*(m+1)

for i in range(m+1):
    # c[n+m-i]=b[m-i]a[n] + (b[m-i+n]a[0]+b[m-i+n-1]a[1]..b[m-i+n-(n-1)]a[n-1])
    c = C[n+m-i]
    for j in range(n):
        if n+m-i-j <= m:
            c -= A[j]*B[n+m-i-j]
    B[m-i] = c//A[(n+m-i)-(m-i)]
print(*B)