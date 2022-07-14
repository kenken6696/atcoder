#!/usr/bin/env python3

H, W = map(int, input().split())
if H == 1 or W == 1:
  print(H*W)
  exit()
k = H//2 + H%2 #横における最大の数
l = W//2 + W%2
print(k*l)