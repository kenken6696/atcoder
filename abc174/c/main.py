#!/usr/bin/env python3

k = int(input())
ans = -1
pre_mod = 7%k
if pre_mod == 0:
    print(1)
    exit()

# modは最大k個の繰り返しである､そのため鳩の巣原理により高々k個確認すれば､少なくとも1つはmod0を確認できる
for i in range(2, k+1):
    pre_mod = (pre_mod*10 + 7)%k
    if pre_mod == 0:
        ans = i
        break
print(ans)