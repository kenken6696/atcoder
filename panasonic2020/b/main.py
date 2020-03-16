#!/usr/bin/env python3
import math

movable = 0
h, w = map(int, input().split())

# 二列ごと見ると全体の半数に移動可能
if h ==1 or w == 1:
    movable = 1
else:
    movable = math.ceil((h * w)/2)

print(movable)