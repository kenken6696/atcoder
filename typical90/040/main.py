#!/usr/bin/env python3

from collections import deque


n, w = map(int, input().split())
A = list(map(int, input().split()))

# 燃やす埋める問題(最小カット問題)
# 1. フォード・ファルカーソン法 O(F|E|)
## 擬多項式時間 残余グラフ上で見つけたs-tパス上にフローを流せるだけ流すという貪欲法
# 2. Jim Orlin法 + KRT O(VE) 2013年のアルゴリズムらしいが実装が見つからず
# 3. Dinic(ディニッツ)法 O(V^2E) 今回はこれでお茶を濁す

# Dinic法について
# 基本的にはFord-Fulkerson法と同じで残余グラフ上で見つけたs-tパス上にフローを最後まで流す
# 違いはFord-Fulkerson法が単純なDFSで増加パスを探索するのに対して､最短経路DAG上で､効率化のためBFSとDFSを併用していること

class Dinic:
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_link(self, _from, to, cap):
        '''to: 行き先, cap:容量, rev:反対側の辺'''
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from])-1])

    def bfs(self, s):
        '''sからの最短距離を探索
        '''
        depth = [-1]*self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap>0 and depth[to]<0:
                    depth[to] = depth[v]+1
                    q.append(to)
        self.depth = depth

    def dfs(self, v, t, flow):
        ''' 増加パスを探索
        '''
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v]>=self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t]<0:
                return flow
            self.progress = [0]*self.n
            current_flow = self.dfs(s, t, float('inf'))
            while current_flow:
                flow += current_flow
                current_flow = self.dfs(s, t, float('inf'))

mf = Dinic(n+2)
for i in range(n):
    mf.add_link(0, i+1, w)
    mf.add_link(i+1, n+1, A[i])
    for j in list(map(int, input().split()))[1:]:
        mf.add_link(i+1, j, 2**63)
print(sum(A)-mf.max_flow(0, n+1))