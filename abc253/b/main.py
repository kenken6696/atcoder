#!/usr/bin/env python3


from collections import Counter


h, w = map(int, input().split())
a_ij, b_ij = [-1, -1], [-1, -1]
found_a = False
for i in range(h):
    s = input()
    cs = Counter(s)
    if cs['o'] == 1:
        if found_a:
            j = s.index('o')
            b_ij = [i, j]
        else:
            found_a = True
            j = s.index('o')
            a_ij = [i, j]
    elif cs['o'] == 2:
        for j in range(w):
            if s[j] == 'o':
                if found_a:
                    b_ij = [i, j]
                else:
                    found_a = True
                    a_ij = [i, j]
ans = abs(a_ij[0]-b_ij[0])+abs(a_ij[1]-b_ij[1])
print(ans)