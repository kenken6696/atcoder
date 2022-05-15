#!/usr/bin/env python3

from collections import defaultdict

n, k = map(int, input().split())
S = [0] + list(map(int, input().split())) # 0埋め､l[i]はO(1)

# 状態管理を初期化のままかどうかで行う
visited = defaultdict(lambda: -1) # [街ナンバー]=テレポート回数
visited[1] = 0
now, not_cycle_c, cycle_c = 1, 0, 0 # --○ 行き先は1つずつなので左図になる
for i in range(1, n+1):
    now = S[now]
    if visited[now] == -1: #未訪問
        visited[now] = i
    else: # サイクルできた時
        if now == 1:
            cycle_c = i
        else:
            cycle_c = i - visited[now]
            not_cycle_c = visited[now] - 1
        break
if not_cycle_c > 0:
    k = (k-not_cycle_c)%cycle_c
else:
    k = k%cycle_c

ans = 1
for _ in range(not_cycle_c+k):
    ans = S[ans]
print(ans)