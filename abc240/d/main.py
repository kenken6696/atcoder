#!/usr/bin/env python3

from collections import deque

n = int(input())
S = list(map(int, input().split()))

dq = deque() # (num, cnt)のque
q_cnt = 0

# なぜか一部でRE､時間切れのため諦める
for i in range(n):
    num = S[i]
    q_cnt += 1
    if i == 0:
        dq.append([num, 1])
    else:
        if num != dq[-1][0]:
            dq.append([num, 1])
        else: # 連続中
            dq[-1][1] += 1
            if num == dq[-1][1]:
                dq.pop()
                q_cnt -= num
    print(q_cnt)

