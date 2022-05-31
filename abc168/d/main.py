#!/usr/bin/env python3

import collections
import heapq


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        # 始点より動的計画法(DP)によりBFS探索して求めていく
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = collections.defaultdict(lambda: float('inf')) # d[i]=iまでの最短経路cost
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = [] # for_BFS q[start]=[[end1, cost1]...]
        heapq.heappush(q, (0, s)) # 始点sの最短経路からのみ探索する
        v = collections.defaultdict(bool) # v[end]=探索済/未探索
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]: # 2回目以降の探索は必ず最短にならない
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

n, m = map(int, input().split())
dik = Dijkstra()
for _ in range(m):
    a, b = map(int, input().split())
    dik.add(a, b, 1)
d = [0]*n
for i in range(1, n):
    path = dik.getDijkstraShortestPath(i+1, 1)
    d[i] = len(path)-1 # start分引く
ans = 'No' if max(d)==0 else 'Yes'
print(ans)
for di in d[1:]:
    print(di)