#!/usr/bin/env python3
import math
a, b, d = map(int, input().split())
cosd, sind = math.cos(math.radians(d)), math.sin(math.radians(d))
x = a*cosd - b*sind
y = b*cosd + a*sind
print(x, y)