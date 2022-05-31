#!/usr/bin/env python3

n, m = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(m) ]
P = list(map(int, input().split()))
ans = 0
for i in range(1<<n):
    switch = [False]*n
    power = [False]*m
    for shift in range(n):
        if i>>shift & 1 == 1:
            switch[shift]=True
    for si, s in enumerate(S):
        k = s[0]
        switch_on = 0
        for ssi in range(1, k+1):
            if switch[s[ssi]-1]:
                switch_on += 1
        if switch_on%2 == P[si]:
            power[si]=True
    if all(power):
        ans += 1

print(ans)



