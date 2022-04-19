#!/usr/bin/env python3

a, b, c, d = map(int, input().split())

# A+C~B+Dで素数があるか探す→どんなC~Dを選んでも､素数を作れないA~Bが1つでもある(真なら高橋Win)
def is_prime(n): # 素数判定 O(√n)
        for i in range(2, n + 1):
            # √nまで調べたらおk(√n以上の因数もったらn超える)
            if i * i > n:
                break
            if n % i == 0:
                return False
        return n != 1
ans_prime = []
i_can_prime = [False]*(b+1) # DP[高橋の値]=true/false(C-D内で素数を作れるか)
for i in range(a+c, b+d+1):
    if is_prime(i):
        ans_prime.append(i)

for i in range(a, b+1):
    for j in range(c,d+1):
        if i+j in ans_prime:
            i_can_prime[i]=True
            break

if False in i_can_prime[a:b+1]:
    print('Takahashi')
else:
    print('Aoki')