#!/usr/bin/env python3

n = int(input())
S = [ list(map(int, input().split())) for _ in range(n) ]


def chebyshev_dist(xy_l):
    """
    チェビシェフ距離を利用して､マンハッタン距離の最大値を返却する
    args: (x, y)のリスト
    return: マンハッタン距離の最大値
    """
    # マンハッタン距離の最大値探索O(n^2)に対して､チェビシェフ距離はO(n)である
    # チェビシェフ距離 = max(abs(x1-x2), abs(y1-y2))

    # チェビシェフ用座標変換
    # (x1, y1),(x2, y2)のマンハッタン距離=(x1+y1, x1-y1),(x2+y2, x2-y2)のチェビシェフ距離
    lenl = len(xy_l)
    cx_l, cy_l = [0]*lenl, [0]*lenl
    for i in range(lenl):
        x, y = xy_l[i]
        cx_l[i], cy_l[i] = x+y, x-y
    # (最大x1-最小x2)とすればxの差の絶対値の差が取れる(yも同様)
    cx_max, cx_min = max(cx_l), min(cx_l)
    cy_max, cy_min = max(cy_l), min(cy_l)
    manhattan_max = max(abs(cx_max-cx_min),abs(cy_max-cy_min))
    return manhattan_max

print(chebyshev_dist(S))