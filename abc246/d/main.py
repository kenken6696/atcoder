#!/usr/bin/env python3
n = int(input())
ans = 10**18

def is_ok(bi, ai):
    if n <= ai**3 + ai**2*bi + ai*bi**2 + bi**3:
        return True
    return False

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, ai):
            ok = mid
        else:
            ng = mid
    return ok

for ai in range(0, 10**6+1):
    bi = meguru_bisect(-1, ai+1) # 式の対称性よりa>=bとしてよい､10**6+1でもAC
    f = ai**3 + ai**2*bi + ai*bi**2 + bi**3
    if f >= n: # ai+1でもだめだったときはスルー
        ans = min(ans, f)
print(ans)