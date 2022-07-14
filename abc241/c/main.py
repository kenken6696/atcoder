#!/usr/bin/env python3

n = int(input())
S = [ input() for _ in range(n) ]

# よこ
for i in range(n):
    for j in range(n-6):
        if S[i][j:j+6].count('.') >= 4:
            print('Yes')
            exit()
# たて
# ななめ
def is_ok(target):
    if 0:
        return True
    else:
        return False

def meguru_bisect(ng, ok, search='min'):
    '''
    めぐる式二部探索
    # args
        ng: とり得る最小の値-1
        ok: とり得る最大の値+1
        search: 'min'(初期値)/'max'
    # return
        条件を満たす最小値(最大値)
        すべて条件を満たさない場合はFalse
    '''
    if search != 'min':
        ng, ok = -1*ok, -1*ng

    is_involved = False
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        target = mid if search == 'min' else -1*mid
        if is_ok(target):
            ok = mid
            is_involved = True
        else:
            ng = mid
    if is_involved:
        return ok if search == 'min' else -1*ok
    else:
        return False