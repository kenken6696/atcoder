#!/usr/bin/env python3

n = int(input())
class_one = [0]*(n+1)
class_two = [0]*(n+1)#クラスごとの累積和
for i in range(1, n+1):
    ci, pi = map(int, input().split())
    if ci == 1:
        class_one[i] = class_one[i-1] + pi
        class_two[i] = class_two[i-1]
    else:
        class_one[i] = class_one[i-1]
        class_two[i] = class_two[i-1] + pi

q = int(input())
for i in range(q):
    s, e = map(int, input().split())
    co = class_one[e] - class_one[s-1]
    ct = class_two[e] - class_two[s-1]
    print(co, ct)