#!/usr/bin/env python3

from copy import deepcopy


n, m, q = map(int, input().split())
D = [ list(map(int, input().split())) for _ in range(m) ]
Q = [ list(map(int, input().split())) for _ in range(q) ]

class Kruskal_UnionFind():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edges = []
        self.rank = [0] * (N+1)
        self.par = [i for i in range(N+1)] # [1]に1を入れる([0]は捨てる)
        self.counter = [1] * (N+1)

    def add(self, u, v, d, i=-1):
        """
        u = from, v = to, d = cost
        """
        self.edges.append([u, v, d, i])

    def root(self, x):
        """
        return: xが属するグループの根
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            z = self.counter[x] + self.counter[y]
            self.counter[x], self.counter[y] = z, z
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def Kruskal(self,q):
        """
        return: 最小全域木のコストの和
        """
        # costでself.edgesを昇順ソートして､サイクルでない辺を順に足していく
        ans = ["No"]*q
        edges = sorted(self.edges, key=lambda x: x[2])
        for i in range(len(edges)):
            e = edges[i]
            if not self.same(e[0], e[1]): # サイクル判定
                if e[3]!=-1:
                    ans[e[3]]="Yes"
                    continue
                self.unite(e[0], e[1])
        return ans

kuf = Kruskal_UnionFind(n)
for d in D:
    kuf.add(d[0], d[1], d[2])
for i, qi in enumerate(Q):
    kuf.add(qi[0], qi[1], qi[2], i=i)
ans = kuf.Kruskal(q)
print(*ans, sep='\n')

