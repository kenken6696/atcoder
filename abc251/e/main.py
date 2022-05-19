#!/usr/bin/env python3

import collections
import heapq


n = int(input())
A = list(map(int, input().split()))
inf = 10**12
# 解1: dp[i][0]=条件を満たす0-iまでの餌やりのうち､A[i]の餌やりをしない時の費用最小値､dp[i][1]=はA[i]ありの時
''' dp = [[0]*2 for _ in range(n)]
# dp[0]のとき､餌やるかやらないかを固定して､それぞれの最小値を考える

# a1ありの場合
dp[0][0], dp[0][1] = inf, A[0]
for i in range(1, n):
    dp[i][0] = dp[i-1][1] # i-1で既に餌やり済
    dp[i][1] = min(dp[i-1])+A[i] # どうせ餌やるので小さい方でよい
ans_with_a1 = min(dp[-1]) # a1で既に1に餌やり済みなので,anは考慮不要

# a1なしの場合
dp[0][0], dp[0][1] = 0, inf
for i in range(1, n):
    dp[i][0] = dp[i-1][1] # i-1で既に餌やり済
    dp[i][1] = min(dp[i-1])+A[i] # どうせ餌やるので小さい方でよい
ans_without_a1 = dp[-1][1] # a1なし､つまり1に餌必要なので,anは必要

print(min(ans_with_a1, ans_without_a1))'''

# 解2 dp[i]=条件を満たす0-iまでの餌やりの時の費用最小値
## 解1では､aiの餌やりをするかしないかの情報を持っていたが､よくよく見ると､
## dp[i][0] = dp[i-1][1] = min(dp[i-2])+A[i-1] であり､
## dp[i] = min(min(dp[i-2])+A[i-1], min(dp[i-1])+A[i]) とかける｡
## つまり､二次元でなく､一次元のdpでよかった!!!!!!


''' # dp[0]のとき､餌やるかやらないかを固定して､それぞれの最小値を考える
# a1あり
dp = [inf]*n
dp[0:2] = [A[0]]*2
for i in range(2,n):
    dp[i] = min(dp[i-2]+A[i-1], dp[i-1]+A[i])
ans_with_a1 = dp[-1]

# a1なし(anあり)
dp = [inf]*n
dp[0:2] = A[-1], A[-1]+min(A[0], A[1])
for i in range(2,n-1):
    dp[i] = min(dp[i-2]+A[i-1], dp[i-1]+A[i])
ans_without_a1 = dp[-2]

print(min(ans_with_a1, ans_without_a1)) '''


# 解3 牛ゲー
## N個の点のうち､始点と終点の最大値を求める問題で､すべての制約が二変数の差分制約式(変数-変数>=定数)のような問題を牛ゲーと呼ぶ｡
## 牛ゲーは相対問題が最短経路問題となっており､相対定理より､この最短経路問題の解が牛ゲーの解となる｡(負辺路なし&s-tパスが存在する時に)
## もしくは､制約式dv+c<=du を見て､制約式の差分が最大になるのは=になるときであり､dvの最短経路問題を

## 2時間かけましたが考えましたがわかりません､書きかけで撤退します
## まだ生きてて暇だったら続きお願いします
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

dik = Dijkstra()
for i in range(n):
    dik.add(i+1, i+3, A[i])
for i in range(n):
    dik.add(i+3, i+1, 0)
_, ans_with_a1 = dik.Dijkstra_search(1)
_, ans_without_a1 = dik.Dijkstra_search(2)


print(min(ans_with_a1, ans_without_a1))