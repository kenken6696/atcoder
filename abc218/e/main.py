#!/usr/bin/env python3

class Kruskal_UnionFind():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edges = []
        self.rank = [0] * (N+1)
        self.par = [i for i in range(N+1)] # [1]に1を入れる([0]は捨てる)
        self.counter = [1] * (N+1)

    def add(self, u, v, d):
        """
        u = from, v = to, d = cost
        """
        self.edges.append([u, v, d])

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

    def size(self, x):
        """
        return: xが属するグループの要素数
        """
        x = self.root(x)
        return self.counter[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def Kruskal(self):
        """
        return: 最小全域木のコストの和
        """
        # costでself.edgesを昇順ソートして､サイクルでない辺を順に足していく
        res = 0
        tmp = 0
        edges = sorted(self.edges, key=lambda x: x[2])
        for i in range(len(edges)):
            e = edges[i]
            if not self.same(e[0], e[1]): # サイクル判定
                self.unite(e[0], e[1])
                res += e[2]
            else:
                if e[2]>0:
                    tmp += e[2]

        return res,tmp

n, m = map(int, input().split())
D = [ list(map(int, input().split())) for _ in range(m) ]
ans = 0

kuf = Kruskal_UnionFind(n)
for d in D:
    kuf.add(d[0], d[1], d[2])
k_c, ans = kuf.Kruskal()
print(ans)