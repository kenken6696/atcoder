class Graph:
    def __init__(self, n, P):
        self.fre = [[] for _ in range(n)]
        self.p = P

    def add(self, x, y):
        self.fre[x-1].append(y)
        self.fre[y-1].append(x)

    def recommend(self, x):
        '''
        return id
        '''
        re_l_p = self.p.copy() # [6,8...]
        x_fre = self.fre[x-1] # 1,4 not index
        re_l_p[x-1] = 0
        for f in x_fre:
            re_l_p[f-1] = 0
        ans = -1
        if max(re_l_p) > 1:
            ans = self.p.index(max(re_l_p)) +1
        return ans

def main():
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    g = Graph(n, P)
    for _ in range(m):
        x, y = map(int, input().split())
        g.add(x, y)
    for i in range(n):
        print(g.recommend(i+1))

if __name__ == '__main__':
    main()