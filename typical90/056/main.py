#!/usr/bin/env python3

n, s = map(int, input().split())
S = [ list(map(int, input().split())) for _ in range(n) ]

# dp作成 買い物計画が可能かどうか
dp = [[False] * (s+1) for _ in range(n+1)] # dp[i][price]=[True/False]
for i in range(1, n+1):
    if i==1:
        dp[i][S[i-1][0]] = True
        dp[i][S[i-1][1]] = True

    for p in range(min(S[i-1]), s+1):
        ai = S[i-1][0]
        bi = S[i-1][1]
        if p-ai>=0 and dp[i-1][p-ai]:
            dp[i][p] = True
        elif p-bi>=0 and dp[i-1][p-bi]:
            dp[i][p] = True

# dp復元 最後まで遡れるかどうか 深さ優先
def dfs(i, p):
    whatbuy, canbuy= '', False
    if i==1:
        if p==S[0][0]:
           return 'A', True
        elif p==S[0][1]:
            return 'B', True
        else:
            return '', False

    ai = S[i-1][0]
    bi = S[i-1][1]
    if p-ai<0 or p-bi<0:
        return '', False

    if dp[i-1][p-ai] or dp[i-1][p-bi]:
        whatbuy, canbuy = dfs(i-1, p-ai)
        if canbuy:
            whatbuy += 'A'
        else:
            whatbuy, canbuy = dfs(i-1, p-bi)
            if canbuy:
                whatbuy += 'B'
    return whatbuy, canbuy

whatbuy, canbuy = dfs(n, s)
if canbuy:
    print(whatbuy)
else:
    print('Impossible')