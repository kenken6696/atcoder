#!/usr/bin/env python3

from collections import deque


h, w = map(int, input().split())
S = [ list(input()) for _ in range(h) ]

def can_move(s):
    if s == '.':
        return True
    else:
        return False

def explore(si, sj):
    dq = deque([[si, sj]]) # BFS用
    route_cnt = [[-1]*w for _ in range(h)] # 始点からの距離 route_cnt[i][j] = 3
    route_cnt[si][sj] = 0

    while len(dq) > 0:
        i, j = dq.pop()
        cnt = route_cnt[i][j]

        if j > 0 and can_move(S[i][j-1]): # 左
            if route_cnt[i][j-1] == -1: # 更新済みなら重複に探索となる
                route_cnt[i][j-1] = cnt + 1
                dq.appendleft([i, j-1])
        if j < w-1 and can_move(S[i][j+1]): # 右
            if route_cnt[i][j+1] == -1: # 更新済みなら重複に探索となる
                route_cnt[i][j+1] = cnt + 1
                dq.appendleft([i, j+1])
        if i > 0 and can_move(S[i-1][j]): # 上
            if route_cnt[i-1][j] == -1: # 更新済みなら重複に探索となる
                route_cnt[i-1][j] = cnt + 1
                dq.appendleft([i-1, j])
        if i < h-1 and can_move(S[i+1][j]): # 下
            if route_cnt[i+1][j] == -1: # 更新済みなら重複に探索となる
                route_cnt[i+1][j] = cnt + 1
                dq.appendleft([i+1, j])

    max_cnt = 0
    for i in range(h):
        max_cnt = max(max_cnt, max(route_cnt[i]))

    return max_cnt

ans = 0
for i in range(h):
    for j in range(w):
        if can_move(S[i][j]):
            ans = max(ans, explore(i, j))
print(ans)