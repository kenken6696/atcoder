#!/usr/bin/env python3
import copy
import numpy as np

h, w, k = map(int, input().split())
original_S = [ list(input()) for _ in range(h) ]
ans = 0

# 全網羅で十分に間に合う
# 行/列を選択するのはbit全探索で実装
# 列を塗るのは､numpyの転置行列を利用する