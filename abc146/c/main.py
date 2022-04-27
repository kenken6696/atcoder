#!/usr/bin/env python3

a, b, x = map(int, input().split())
def is_ok(arg):
    arg = arg * -1
    if x >= a*arg + b*len(str(arg)):
        return True
    else: return False

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

max_n = -(meguru_bisect(-1*(10**9+1), 0))
print(max_n)