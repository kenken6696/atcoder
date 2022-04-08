#!/usr/bin/env python3
from re import I
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from atcoder.abc245.f.main import make_divisors

n, m = map(int, input().split())
edge = np.array([input().split() for _ in range(m)], dtype=np.int64).T

# 強連結成分分解 SCC, Strongly Connected Component
tmp = np.ones(m, dtype=np.int64).T
graph = csr_matrix((tmp, (edge[:] -1)), (n,n))
vertex, labels  = connected_components(graph, directed = True, connection = 'strong')
# directd 有向無向､ connection 両方向片方向

is_ssc=[]
for i in range(n):
    if i == 0:
        i_n = labels[i]
        i_c = 1
        continue

    if labels[i] == i_n:
        # 前回と同じなら､強連結成分
        i_c += 1
        is_ssc[i-1] = 1
    else:
        if i_c == 1:
            # 強連結成分でない
            is_ssc[i-1] = 0
        else:
            # 強連結成分終わり
            is_ssc[i-1] = 1

        i_n = is_ssc[i]
        i_c = 1

# 強連結成分に到達できる頂点
connected_ssc = is_ssc