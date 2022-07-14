#!/usr/bin/env python3
import numpy as np
n, k = map(int, input().split())

for _ in range(k):
    n = int(str(n), 8) #8⇒10
    n = np.base_repr(n, base=9) #10⇒9
    n = int(str(n).replace('8', '5')) #8扱い

print(n)