n, m = map(int, input().split())
A = [ int(input()) for _ in range(n) ] # ゴンドラ
B = [ int(input()) for _ in range(m) ] # group
C = [0]*n
now_g = 0
def next_g(i):
    nxt = i+1 if i <= (n-2) else 0
    return nxt

for b in B:
    while b>0:
        if A[now_g]<b:
            C[now_g] += A[now_g]
        else:
            C[now_g] += b
        b -= A[now_g]
        now_g = next_g(now_g)

for c in C:
    print(c)

