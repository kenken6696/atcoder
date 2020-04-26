#!/usr/bin/env python3

t_hp, t_ap, a_hp, a_ap = map(int, input().split())
while True:
    if a_hp <= t_ap:
        print('Yes')
        break
    if t_hp <= a_ap:
        print('No')
        break

    a_hp -= t_ap
    t_hp -= a_ap