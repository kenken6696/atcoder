#!/usr/bin/env python3

import collections
import heapq
from math import ceil


n, m, x, y = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(m) ]
# ダイクストラ
class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, t, k, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, t, k])
            self.e[v].append([u, t, k])

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #始点より動的計画法(DP)によりBFS探索して求めていく
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = collections.defaultdict(lambda: float('inf')) # d[i]=iまでの最短経路cost
        d[s] = 0
        q = [] # for_BFS q[start]=[[end1, cost1]...]
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool) # v[end]=探索済/未探索
        while len(q):
            time, u = heapq.heappop(q)
            if v[u]: # 2回目以降の探索は必ず最短にならない
                continue
            v[u] = True

            for uv, ut, uk in self.e[u]:
                if v[uv]:
                    continue
                arrivetime = ceil(time/uk)*uk+ut
                if d[uv] > arrivetime:
                    d[uv] = arrivetime
                    heapq.heappush(q, (arrivetime, uv))

        return d

dik = Dijkstra()
for s in S:
    a, b, t, k = s
    dik.add(a, b, t, k)
d = dik.Dijkstra_search(x)
if d[y]==float('inf'):
    print(-1)
else:
    print(d[y])