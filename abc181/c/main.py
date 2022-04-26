#!/usr/bin/env python3

n = int(input())
S = [ list(map(int, input().split())) for _ in range(n) ]
for a in range(n):
    for b in range(a+1, n):
        for c in range(n):
            if a == c or b == c:
                continue
            if (S[c][1]-S[a][1])*(S[b][0]-S[a][0])==(S[b][1]-S[a][1])*(S[c][0]-S[a][0]):
                print("Yes")
                exit()
print("No")