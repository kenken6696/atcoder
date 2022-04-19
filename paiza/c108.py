n = int(input())
X = [ int(input()) for _ in range(n)]
C = [ list(map(int, input().split())) for _ in range(n) ]
k = int(input())
Y = [ int(input()) for _ in range(k)]
ans = 0
for i in range(k-1):
    d, nxtd = Y[i], Y[i+1]
    ans += X[d-1] + C[d-1][nxtd-1]
ans += X[Y[-1]-1]
print(ans)