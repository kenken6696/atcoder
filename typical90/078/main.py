#!/usr/bin/env python3

from bisect import bisect_left
import collections
import heapq


n, m = map(int, input().split())

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
            self.e[u].append(v)
            self.e[v].append(u)

    def resolve(self):
        """
        #0-indexedでなくてもよいことに注意
        #自分自身より頂点番号が小さい隣接頂点がちょうど 1 つ存在する
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        ans = 0
        for i in range(1, n+1):
            if bisect_left(sorted(self.e[i]), i)==1:
                ans += 1
        return ans

dik = Dijkstra()
for i in range(m):
    x, y = map(int, input().split())
    dik.add(x, y, 1)
ans = dik.resolve()
print(ans)