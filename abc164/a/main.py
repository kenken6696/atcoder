#!/usr/bin/env python3

s, w = map(int, input().split())

if s <= w:
    print('unsafe')
else:
    print('safe')