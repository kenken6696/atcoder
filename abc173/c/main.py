#!/usr/bin/env python3
import copy
import numpy as np

h, w, k = map(int, input().split())
original_S = [ list(input()) for _ in range(h) ]
ans = 0

## 塗る塗らないを[10100](右から左)として管理
for hi in range(1<<h): # 1<<nは､2**n+1と同値
    S = copy.deepcopy(original_S)
    for hshift in range(h): # 列(行)ごとに確認
        if hi>>hshift & 1 == 1:
            S[hshift] = ['r']*w
    S_h = copy.deepcopy(S)
    for wi in range(1<<w): # 1<<nは､2**n+1と同値
        S = copy.deepcopy(S_h)
        S_t = np.array(S).T.tolist()
        for wshift in range(w): # 列(行)ごとに確認
            if wi>>wshift & 1 == 1:
                S_t[wshift] = ['r']*h
        S = np.array(S_t).T.tolist()

        black = 0
        for hii in range(h):
            for wii in range(w):
                if S[hii][wii] == '#':
                    black += 1
        if black == k:
            ans += 1
print(ans)