## 進め方


```
# 入力
B = int(input())
A, B, C = map(int, input().split())
L = list(map(int, input().split())) # [0]+して0埋めも検討
L = [list(map(int, input().split())) for _ in range(N)]

# 出力
# listの出力
print(list, *list(sep=''), ','.join(map(str, list)))
# [1, 2] 12 1,2
# 逆順
s = 'str'
print(s[::-1]) # rts

# アンパック
a = 1,2 # タプルなどは展開され引数に格納される
a, *b = 1, 2, 3, 4 # b=(2,3,4)と無制限に引数を受け付ける
num1, num2, num3 = *b # *は展開も可能
**kwagrs = **dic # **はキーワード引数のみ格納可能､展開不可

# 進数､論理和/論理積/排他的論理積
bin(n), oct(n), hex(n) # 9=0b101, 2進数､8進数､16進数
int('101', 2) # 2進数⇒10進数
0b101>>2 # 右bitシフト 0b1=1
0b101<<2 # 左bitシフト 0b10100=20
1&9 # AND 001&101=001
1|9 # OR 001|101=101
1^9 # XOR 001|101=100

# 条件
if a and b or c and d:
# and処理 -> or処理 となる
# (a and b) or (c and d)

# 繰り返し文
for index, list in enumerate(lists):
    print(str(index+1) + '番目：' + list)
## 三項演算子
x = '偶数' if num % 2 == 0 else '奇数'

# 数え上げ
prdct = itertools.product('abc', repeat=2) # 順列重複あり
pmt = itertools.permutations('abc', 2) # 順列重複なし
cmbs = itertools.combinations_with_replacement('abc', 2) #組み合わせ重複あり
cmbs = itertools.combinations('abc', 2) #組み合わせ重複なし

# 累積和/いもす法
# 複数回クエリする時は､累積和+[0]を計算しておくほうがはやい
# 1次元
L = list(range(1,7)) # [1,2,3,4,5,6]
AC = list(itertools.accumulate(L))+[0] # [1,3,6,10,15,21,0]
print(AC[4]-AC[0-1]) # 15 (AC[4]-AC[-1]→15-0→15)


# 数値計算

# 正確な計算
## 16桁未満はint/floatでおk､問題は16桁以上
from fractions import Fraction
x = Fraction('1')/Fraction('3')
print('{:.9f}'.format(float(x))) #小数点9桁切り捨て

# 整数化処理
round(x) # 四捨五入
A//B # 整数切り捨て
-(-1*A//B) # 整数切り上げ

# 累乗
a ** b # これでもいいが､powが10倍はやい
pow(a,b,c) # a**b%c
30%3 == (10%3+20%3)%3 # 最後にmodするなら､初めからmodして良いし早い

# 階乗
math.factorial(n)

# 最大公約数/最小公倍数 3.9-
math.gcd(a,b)
math.lcm(a,b)
# 配列
# 初期化
a=[0]*2 ,b=[[0]*2], c=[[0]]*2
# a=[0,0], b=[[0,0]], c=[[0],[0]]

# 2次元配列
# 初期化
l_2d_ok = [[0] * 4 for i in range(3)]
l_2d_ng = [[0] * 4 ] * 3 # これだと同じオブジェクトになってしまう

# copy
new_list = old_list  # newへの操作はすべてoldにも影響でる
new_list = copy.copy(old_list)  # oldの要素を変えるとnewも変更される
new_list = copy.deepcopy(old_list)  # oldの要素を変えてもnewは変更されない

# 転置行列
X_t = np.array(X).T.tolist()

# カウント
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
len(l) # 7
l.count('a') # 4

c = collections.Counter(l) # Counter({'a': 4, 'c': 2, 'b': 1})
c.items() # dict_items([('a', 4), ('b', 1), ('c', 2)])
c['a'] # 4
c.most_common() # [('a', 4), ('c', 2), ('b', 1)]
c.most_common(2) # [('a', 4), ('c', 2)]
values, counts = zip(*most_common())
# ソート
L = [[1,2,3],[2,3,4],[3,4,5]]
L = sorted(L, reverse=True, key=lambda x: x[1])  #[1]に注目して降順ソート

# ソート済み配列に挿入
bisect.insort_left(A, x)
# 配列ソートはO(nlogn),対して二部探索はO(logn)
# A.insert(bisect.bisect_left(A,x))と同じ

# キュー
## dequeを使うが､添字アクセス両端はO(1)だが､中央はO(n)
from collections import deque
d = deque(['m', 'n']) # 尺取法などにも

## 配列の最小値(最大値)
### Priority queue heap化 O(nlong), 最小値 O(1), 挿入/削除 O(logn)
S = list(map(lambda x: x*-1, S)) # 最大値用
heapq.heapify(S) # 優先度付きqueに変換
heapq.heappop(S) # 最小値取り出し
heapq.heappush(S, -2)  # 要素の挿入
### 配列がある数値以上か確認
if min(l) > x:


# dict
from collections import defaultdict
d = deaultdict(int) # keyerr避けにこっちつかお
d = deaultdict(lambda:5) # 初期値は関数指定
d = deaultdict(lambda:deaultdict(list))
d['key'] == d.get('key')
d = dict(d) # keycheckや存在確認欲しかったらdictへ

# _の使い方
def init_(x): # 後1 予約語の使用
def _my_method(x): # 前1 private化のつもり(システム上区別なし)
__my_variable='s' # 前2 マンダリング,ちょっとprivate化(システム上区別あり)
def __func__: # 前2後2 magic method(システムが呼ぶ用)

#DPまとめ
## 最長増加部分列LIS
数列のうち､順番通りに取り出して増加列となる列数最大数を求める
数列の最終要素の最小値を更新していく
実装はbisectのDP置換によって可能
降順は､昇順の求めてreverseすればよい
```
    dp_i = bisect.bisect_right(dp, C[i]-1) # 最長増加部分列(同数ng)
    dp_i = bisect.bisect_right(dp, C[i]) # 広義最長増加部分列(同数おk)
    dp[dp_i] = C[i] # 更新を考慮するため挿入ではなく置換
dp_size = bisect.bisect_left(dp, INF-1)
```
## 最長共通部分列LCS
複数の文字列のうち､共通部分の列数最大数を求める
DP[L1][L2]を利用して格納する

# ACL-for-python
# 中国剰余定理
```
#3で割ると2余り、5で割ると3余り、7で割ると2余る
C = [3,5,7]#これで割ったら
R = [2,3,2]#この余りになる対のリスト
r,m = crt(R,C)
```
https://qiita.com/H20/items/1a066e242815961cd043#8%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB%E6%B3%95%E6%9C%80%E5%B0%8F%E5%85%A8%E5%9F%9F%E6%9C%A8
まだやってないやつ
6 bit探索
29-32
34-37
42

```