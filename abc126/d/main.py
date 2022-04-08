#!/usr/bin/env python3

from distutils.errors import CCompilerError
from os import closerange


n = int(input())
dist_list = [ list(map(int, input().split())) for _ in range(n-1) ]
color_list = [ 9 for _ in range(n) ] # 9は初期値

color_list[dist_list[0][0] - 1] = 0 # u1のみ0で塗る

while 9 in color_list: # 初期値がなくなるまで繰り返し
    for d in dist_list:
        if color_list[d[0]-1] == 9 and color_list[d[1]-1] == 9:
            continue # 両方未定なら塗れない
        elif color_list[d[0]-1] != 9 and color_list[d[1]-1] != 9:
            continue # 両方塗り済みなら必要なし
        else: #どちらか塗ってる
            if color_list[d[0]-1] != 9: #u側が塗っている
                if d[2]%2 == 0: # 距離偶数なので同じ色
                    color_list[d[1]-1] = 0 if color_list[d[0]-1] == 0 else 1
                else: # 距離奇数なので違う色
                    color_list[d[1]-1] = 1 if color_list[d[0]-1] == 0 else 0
            else: # v側が塗っている
                if d[2]%2 == 0: # 距離偶数なので同じ色
                    color_list[d[0]-1] = 0 if color_list[d[1]-1] == 0 else 1
                else: # 距離奇数なので違う色
                    color_list[d[0]-1] = 1 if color_list[d[1]-1] == 0 else 0

for i in color_list:
    print(i)