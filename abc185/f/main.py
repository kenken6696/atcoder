#!/usr/bin/env python3

n, q = map(int, input().split())
S = list(map(int, input().split()))
Q = [ list(map(int, input().split())) for _ in range(q) ]

class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        '''[l,r)区間の処理結果を返す'''
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        '''全区間の処理結果を返す'''
        return self.d[1]
    def max_right(self,l,f):
        '''[l:]区間の関数fの結果が変わる切れ目を返す'''
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        '''[:r]区間の関数fの結果が変わる切れ目を返す'''
        assert 0<=r and r<self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 & (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])
'''
#add
G=segtree(S,(lambda x,y:x+y),0)
#times
G=segtree(S,(lambda x,y:x*y),1)
#min
G=segtree(S,min,INF)
#max
G=segtree(S,max,-INF)
#gcd
from math import gcd
G=segtree(S,gcd,0)
#lcm
from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
G=segtree(S,lcm,1)
# xor
G=segtree(S,(lambda x,y:x^y),0)
# or
G=segtree(S,(lambda x,y:x|y),0)
# and
N=30
G=segtree(S,(lambda x,y:x&y),(1<<N)-1)
'''
# xor
G=segtree(S,(lambda x,y:x^y),0)
ans_l = []
for i in range(q):
    t, x, y = Q[i]
    if t == 1:
        G.set(x-1, G.get(x-1)^y)
    else:
        print(G.prod(x-1, y))