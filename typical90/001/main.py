#!/usr/bin/env python3

def is_ok(m):
    # k+1個をすべてm以上にできたらおk
    # mは-値のため､-1がけする
    m *= -1
    cnt,pre_l = 0, 0
    for i in range(n+1):
        if i == n:
            if l-pre_l >= m:
                cnt += 1
        else:
            if A[i]-pre_l >= m:
                pre_l = A[i]
                cnt += 1
    if cnt >= k+1:
        return True
    else:
        return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    すべてngだった場合の管理はしていない
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))

ans = meguru_bisect(-l-1,1) #最大値算出のため-がけ
print(-1*ans)