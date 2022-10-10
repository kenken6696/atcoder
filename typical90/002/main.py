#!/usr/bin/env python3

n = int(input())
if n%2 == 1:
    exit()

# 一番端の()の中をbit全探索して､ifで弾く
mid_l = []
for i in range(1<<(n-2)): #並べ方ごと
    mid = ''
    leftn = 1
    comp_f = True
    for shift in range(n-2): #場所ごと
        if i>>shift & 1 == 1: #1なら(
            mid += '('
            leftn += 1
        else: #0なら)
            if leftn > 0:
                mid += ')'
                leftn -= 1
            else:
                comp_f = False
                break
    if comp_f and leftn == 1:
        mid_l.append(mid)

ans = []
for m in mid_l:
    ans.append('('+m+')')
ans.sort()
for a in ans:
    print(a)