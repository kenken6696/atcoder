import itertools
import numpy as np

n, l = map(int, input().split())
X = [ list(map(int, input().split())) for _ in range(n) ]
X_t = np.array(X).T.tolist()

for i in range(1, l+1): # i個の特徴ですべて場合分けできるか調べる
    cmbs = itertools.combinations(range(l), i) #組み合わせ重複なし
    for cmb in cmbs: # i個の特徴組み合わせの中ですべてを場合できるものが存在するか
        searched = set()
        tmp = []
        for li in cmb:
            tmp.append(X_t[li])
        tmp_t = np.array(tmp).T.tolist()
        for tmpi in tmp_t:
            searched.add(tuple(tmpi))
        if len(searched)==n:
            print(len(cmb))
            exit()
