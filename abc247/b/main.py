#!/usr/bin/env python3
n=int(input())
S = [ list(input().split()) for _ in range(n) ]
all_name = []
check_name = []
for i in range(n):
    all_name.append(S[i][0])
    all_name.append(S[i][1])

for i in range(n):
    check_name = all_name[0:2*i]+all_name[(i+1)*2:]
    if check_name.count(S[i][0])>0:
        if check_name.count(S[i][1])>0:
                print('No')
                exit()
print('Yes')
