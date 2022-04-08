import sys
input=sys.stdin.readline

n=int(input())
c=[]

for i in range(n):
  c.append(int(input()))

import bisect
def LIS(a):
  lis=[a[0]]
  for aa in a:
    if lis[-1]<aa:
      lis.append(aa)
    else:
      lis[bisect.bisect_left(lis,aa)]=aa
  return lis

l=len(LIS(c))

print(n-l)