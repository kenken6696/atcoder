#!/usr/bin/env python3

from collections import defaultdict, deque

n, m = map(int, input().split())
d = defaultdict(list) # d[出発点]=[行き先リスト] not indent
ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
def bfs(start): # 出発点からの組み合わせ数を返す
    visited = [False]*(n+1) # 0埋め
    visited[start] = True
    cnt = 1
    dq = deque([start]) # 行き先管理

    while len(dq) > 0: # 行き先を右詰めにしてBFS
        now = dq.popleft()
        for to in d[now]:
            if visited[to] == False:
                visited[to] = True
                cnt += 1
                dq.append(to)
    return cnt

for i in range(1, n+1):
    ans += bfs(i)
print(ans)