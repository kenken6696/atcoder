#!/usr/bin/env python3

n = int(input())
sl = [0]+list(input())
qn = int(input())
Q = [ list(map(int, input().split())) for _ in range(qn) ]
is_reversed = False

for q in Q:
    if q[0] == 1:
        a, b = q[1], q[2]
        if is_reversed:
            if a>n: # n<a<b
                a -= n
                b -= n
            elif b>n: # a<n<b
                a += n
                b -= n
            else: # a<b<=n
                a += n
                b += n
        sl[a], sl[b] = sl[b], sl[a]
    else:
        if is_reversed:
            is_reversed = False
        else:
            is_reversed = True
ans = []
if is_reversed:
    ans = sl[n+1:] + sl[1:n+1]
else:
    ans = sl[1:]
print(''.join(ans))