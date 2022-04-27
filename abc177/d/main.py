#!/usr/bin/env python3

class UnionFind:
    def __init__(self, n):
        self.siz = [0]+[1]*(n) # 配列調整のため前空け
        self.par = [0]+[-1]*(n) # 最初は皆､根

    def root(self, x):
        # 根を返す
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        # 根を確認して､和集合する
        x = self.root(x)
        y = self.root(y)

        if x == y: # 既に同じ集合なら処理不要
            return

        # union by size(x側頂点数>=y側頂点数 にする)
        if self.siz[x] < self.siz[y]:
            x, y = y, x # swap

        # yをxの子にする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return

def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.unite(x, y)
    print(max(uf.siz))

if __name__ == '__main__':
    main()