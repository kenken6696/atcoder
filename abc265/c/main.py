#!/usr/bin/env python3

h, w = map(int, input().split())
S = [ list(input()) for _ in range(h) ]

passed = set()
nextij = (0, 0)
while nextij not in passed:
    passed.add(nextij)
    nxt = S[nextij[0]][nextij[1]]
    if nxt == 'U':
        if nextij[0]>0:
            nextij = (nextij[0]-1, nextij[1])
        else:
            print(nextij[0]+1, nextij[1]+1)
            exit()
    elif nxt == 'D':
        if nextij[0]<h-1:
            nextij = (nextij[0]+1, nextij[1])
        else:
            print(nextij[0]+1, nextij[1]+1)
            exit()
    elif nxt == 'L':
        if nextij[1]>0:
            nextij = (nextij[0], nextij[1]-1)
        else:
            print(nextij[0]+1, nextij[1]+1)
            exit()
    else:
        if nextij[1]<w-1:
            nextij = (nextij[0], nextij[1]+1)
        else:
            print(nextij[0]+1, nextij[1]+1)
            exit()

print(-1)
