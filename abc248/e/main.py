#!/usr/bin/env python3
import itertools
from fractions import Fraction
n, k = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]
ans = set()

def calc_liner(x1,y1,x2,y2):
    x_d = Fraction(x2-x1)
    y_d = Fraction(y2-y1)
    if x_d==0:
        return 'x', 0
    elif y_d==0:
        return 'y', 0
    else:
        d = (y_d)/(x_d)
        return d, y1-d*x1

if k == 1:
    print('Infinity')
    exit()
check_cmb = itertools.combinations_with_replacement(S, k) #組み合わせ重複あり⇒これだと(1,2)(2,1)が出てきて処理増えるので×
for cmb in check_cmb:
    d, a = calc_liner(cmb[0][0],cmb[0][1],cmb[1][0],cmb[1][1])
    if (d, a) in ans: # 重複する場合は確認する必要なし
        continue
    if k == 2:
        ans.add((d, a))
        continue
    if d=='x':
        for i in range(2, k):
            if cmb[0][0] != cmb[i][0]:
                break
    elif d=='y':
        for i in range(2, k):
            if cmb[0][1] != cmb[i][1]:
                break
    else:
        for i in range(2, k):
            di, ai = calc_liner(cmb[0][0],cmb[0][1],cmb[i][0],cmb[i][1])
            if d!=di or a!=ai:
                break
    ans.add((d, a))
print(len(ans))