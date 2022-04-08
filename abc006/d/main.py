#!/usr/bin/env python3
import bisect

n = int(input())
C = [ int(input()) for _ in range(n) ]

# 最長増加部分列LISを求めて､抜けている分が操作必要
dp = [ 4*10**4 ] * (n+1)
for i in range(n):
    index = bisect.bisect_left(dp, C[i])
    dp[index] = C[i] # 更新を考慮するため挿入ではなく置換

dp_size = bisect.bisect_left(dp, 4*10**4-1)
ans = n - len(dp[:dp_size])

print(ans)