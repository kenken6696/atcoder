#!/usr/bin/env python3

n,m  = map(int, input().split())
l = [ list(map(int, input().split())) for _ in range(m) ]

inf = float('inf')
class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])


    def BellmanFord_search(self, start):
        """
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        #  infならたどり着けず
        # -infなら"通りたいパスに"負の閉路が存在する
        D = [inf for _ in range(self.N)]
        D[start-1] = 0
        for i in range(self.N*2):
            for u,v,d in self.edges:
                if D[v-1] > D[u-1] + d:
                    D[v-1] = D[u-1] + d
                    #2巡目負経路が存在する場合の動き
                    if i>=self.N:
                        D[v-1]=-inf
        return D

bf = BellmanFord(n)
for m in l:
    bf.add(m[0], m[1], m[2]*-1, directed=True) # 最大距離を求めるため-1かけて最短を求める
shortest_d = bf.BellmanFord_search(1) # 頂点1からの各最短距離
print(shortest_d[n-1]*-1) # -1かけてもとに戻す