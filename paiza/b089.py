n, m = map(int, input().split())
S = [ input() for _ in range(n) ]
W = [ input() for _ in range(m) ]

def search(w):
    for i in range(n):
        for j in range(n):
            if S[i][j] == w[0] and i+len(w)<=n and j+len(w)<=n:
                for k in range(1, len(w)):
                    if S[i+k][j+k] != w[k]:
                        break
                return [j+1, i+1]

for w in W:
    print(*search(w))
