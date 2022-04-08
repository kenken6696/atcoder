#!/usr/bin/env python3

n, m = map(int, input().split())
l = list(map(int, input().split()))
bc_l = [ list(map(int, input().split())) for _ in range(m) ]

for bc in bc_l:
    l += [ bc[1] ] * bc[0]
l.sort(reverse=True)
print(sum(l[:n]))

"""
時間切れになるので､上の別解を採用
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))

bc_l = [ list(map(int, input().split())) for _ in range(m) ]
bc_l.sort(key=lambda x:x[1], reverse=True)

for bc in bc_l:

    for i in reversed(range(bc[0])):
        if l[i] < bc[1]:
            index = bisect.bisect_right(l, bc[1], i)
            for _ in range(i+1):
                l.insert(index, bc[1])
            l = l[i+1:]
            break

print(sum(l)) """