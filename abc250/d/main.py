#!/usr/bin/env python3

n = int(input())

def is_prime(n): # 素数判定 O(√n)
    for i in range(2, n + 1):
        # √nまで調べたらおk(√n以上の因数もったらn超える)
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1
def sieve_prime(n): # 素数数え上げ
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table

def is_ok(p, primes, target):
    if p*primes[target]**3>n:
        return False
    else:
        return True

def meguru_bisect(p, primes, ng, ok, search='min'):
    '''
    めぐる式二部探索
    # args
        ng: とり得る最小の値-1
        ok: とり得る最大の値+1
        search: 'min'(初期値)/'max'
    # return
        条件を満たす最小値(最大値)
        すべて条件を満たさない場合はFalse
    '''
    if search == 'max':
        ng, ok = -1*ok, -1*ng

    is_involved = False
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        target = mid if search == 'min' else -1*mid
        if is_ok(p, primes, target):
            ok = mid
            is_involved = True
        else:
            ng = mid
    if is_involved:
        return ok if search == 'min' else -1*ok
    else:
        return False

s = 10**6
if n < s:
    s = n
_, primes = sieve_prime(s)
primes_num = len(primes)
ans = 0
for i in range(primes_num-1):
    p = primes[i]
    q_start = primes[i+1]
    if p*q_start**3>n:
        break
    elif p*q_start**3==n:
        ans += 1
        break
    else:
        q_end_i = meguru_bisect(p, primes, (i+1), primes_num, search='max')
        if q_end_i != False:
            ans += (q_end_i - i)
        else:
            ans += 1
print(ans)

def is_ok(target):
    if 0:
        return True
    else:
        return False