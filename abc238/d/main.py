#!/usr/bin/env python3

n = int(input())
S = [ list(map(int, input().split())) for _ in range(n) ]

for i in range(n):
    ans = 'No'
    a, s = S[i]
    # 非負の2変数問題であるが､論理積の特性によりx=a⇒y=s-aとしてよい
    if s-a>=0 and a&(s-a)==a:
        ans = 'Yes'
    print(ans)
