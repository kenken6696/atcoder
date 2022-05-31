#!/usr/bin/env python3

from collections import defaultdict
import heapq


q = int(input())
min_num, max_num = [],[]
heapq.heapify(min_num)
heapq.heapify(max_num)
s = defaultdict(int)
for i in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        if s[l[1]] > 0:
            s[l[1]] += 1
        else:
            s[l[1]] += 1
            heapq.heappush(min_num, l[1])
            heapq.heappush(max_num, -1*l[1])
    elif l[0] == 2:
        if s[l[1]] > l[2]: # まだ残るので更新不要
            s[l[1]] -= l[2]
        else:
            s[l[1]] = 0

    else:
        now_max, now_min = 0, 0
        while max_num:
            temp_max = -1*(heapq.heappop(max_num))
            if s[temp_max] > 0:
                now_max = temp_max
                heapq.heappush(max_num, -1*now_max)
                break
        while min_num:
            temp_min = heapq.heappop(min_num)
            if s[temp_min] > 0:
                now_min = temp_min
                heapq.heappush(min_num, now_min)
                break
        print(now_max-now_min)