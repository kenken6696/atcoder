# Python Tips

## 入力/出力/代入
```
# 入力
B = int(input())
A, B, C = map(int, input().split())
L = list(map(int, input().split())) # [0]+して0埋めも検討
L = [list(map(int, input().split())) for _ in range(N)]

A=B=3 # 連続代入 AもBも3

# 出力
# f文字列(Python3.6-)
print(f'文字列と{hensu1} /n を混ぜて書けるよ') # 改行文字列はspaceで開ける
# listの出力
print(list, *list, sep='\n'), ','.join(map(str, list)))
# [1, 2] 1(改行)2 1,2
# 逆順
s = 'str'
print(s[::-1]) # rts

# アンパック(代入)
a = 1,2 # タプルなどは展開され引数に格納される
a, *b = 1, 2, 3, 4 # b=(2,3,4)と無制限に引数を受け付ける
num1, num2, num3 = *b # *は展開も可能
**kwagrs = **dic # **はキーワード引数のみ格納可能､展開不可
```
## ファイル入出力
```
with open('sample.txt') as f: # with構文だとclose不要,modeのデフォルトがrなので指定不要
    contents = f.read() # 全部読みこみ
    line = f.readline() # 1行だけ読み込み
    lines = f.readlines() # 行ごとにlistで読み込み

with open('sample.txt', mode='w') as f: # 引数に",
    f.write(string)
    f.writelines(list)

```
## 文字列
```
# 整形/空白･改行削除
s = s.replace('\n', '\t') #改行をtabに
s_list = s_list.split()

# 文字コード変換
c = chr(219) # asc2 to chr
ord(c) = # chr to asc2

# アルファベット判定
import string
list(string.ascii_lowercase)

# ランダムシャッフル
import random
print(random.shuffle(l))
# 置換
""Hello World!! Hello Python"".replace("Hello", "Hey!!")
```

## 繰り返し

```
## for文
for i in range(5):

## 拡張for文(index呼び出し省略したい時)
for a in A: # A=[1,2,..]
for k, v in Dict.items():

## enumarate(indexも欲しい時)
for i, a in enumerate(A):

## zip(iterable2つを同時に処理したい時)
for a, b in zip(A, B): # 配列の長さは短い方が優先される
for a, b in zip_longest(A,B, fillvalue=10) # 長い方優先,fillvalue(初期値None)で穴埋め
for c in zip(A, B): # タブルc=(a,b)となる

## 便利な使い方
for i, (a, b) in enumerate(zip(A, B)) # zipでenumerate
d = dict(zip(A, B)) # 配列の辞書化 d[a]=b
two_d_l_T = list(zip(*two_d_l)) # 転置行列化
```

## 条件
```
## 0以上orTrueのとき条件文を省略できる
if a: # a>0 or a==True

## 三項演算子
x = '偶数' if num % 2 == 0 else '奇数'

## 複数条件(and処理->or処理)
if a and b or c and d:
# (a and b) or (c and d)
```

## 配列
```
# 初期化
a=[0]*2 ,b=[[0]*2], c=[[0]]*2
# a=[0,0], b=[[0,0]], c=[[0],[0]]

# slice
n_l = [i for i in range(5)]
n_l[1:-1:2] # [start:end:step]
n_l[::] #初期値は[0:len(n_l):1]

# 逆順
l[::-1] # step=-1でOK
l.reverse() # 破壊的/何も返さない
for i in reversed(l) # iterを逆順にする

# 検索
l.index('ans') # 最初のindexを返す
def my_index(l, x, default=False): #エラー避け
    return l.index(x) if x in l else default

[i for i, x in enumerate(l) if x == 'a'] # 全てのindexを返す

# 削除
del l[0:2] # index
l.remove('want_del') # 最初のvalueを削除


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
two_d_l_T = list(zip(*two_d_l)) # 転置行列化

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

## 配列の最小値(最大値)(管理)
### Priority queue heap化 O(nlong), 最小値 O(1), 挿入/削除 O(logn)
S = list(map(lambda x: x*-1, S)) # 最大値用
heapq.heapify(S) # 優先度付きqueに変換
heapq.heappop(S) # 最小値取り出し
heapq.heappush(S, -2)  # 要素の挿入
heappush(S, (5, 'write code')) # 数値を前にしたtupleも可能(dijkstraなどで使用)
### 配列がある数値以上か確認
if min(l) > x:
### 配列のTrue/Falseチェック
all([True, True]) # すべてTrueか確認 ->True
any([True, False]) # いずれかTrueか確認
not any([False, False]) # すべてFalseか確認

## 配列の比較
## Dictに持ち直してもO(a*b)かかるため､ハッシュ値の総和で比較する
s = (s + a * (a + 1346) * (a + 9185)) % (8128812800000059)
```
## numpy(1次元)
```
# 初期化
import numpy as np
arr = np.array(l) # 固定長の配列
arr_r = np.arange(3) # [0 1 2]

arr_ones = np.ones(3, dtype=np.int32) # [1 1 1] デフォだと少数
arr_zeros = np.zeros(0) #[](空配列)
arr_ones_like = np.ones_like(arr) # 同じ要素数の配列を作れる

arr_lin = np.linspace(0, 1, 3) #[0. 0.500 1.] endpoint=Falseで終点無視
arr_rnd = np.random.rand(10) #一様分布から10個の乱数作成
arr_rndn = np.random.randn(10) #正規分布からの乱数作成

arr_full = np.full(5, 0.1) #ones(n)*aと同値だが定数倍高速
arr_empty = np.empty(10) #zeros(n)に代入するより定数倍高速だが､初期値がランダム値

# 操作
## 確認
arr.size #要素数
arr.shape #(行､列)
arr.ndim #列数
## 代入
arr_ones[1]=3 #[1. 3. 1.]
arr_zeros[1:] = 1 #[0 1. 1.]/ブロードキャスト
## 結合
np.concatenate([arr1, arr2])(listなら足し算だが)
## 分割
np.split(arr, 3) #3等分
np.split(arr, [:3,]) #指定indexで分割
## 演算
arr1_arr2_10 = arr1**arr2+10 #配列ごと四則演算できる
arr[1:4] += 5 #スライスした要素にも演算可能
np.exp(arr)#配列ごと関数演算も可能
arr[arr>0].sum() #0以上の合計値
(arr>0).astype(np.int32).sum() # 0以上の要素数

np.isclose(arr1, arr2) #浮動小数点誤差を考慮した比較

## 切り捨て/丸め
math.floor(arr) #小数点切り捨て(return int)
math.ceil(arr) #小数点切り上げ(return int)
np.round(arr, -1) #1桁目で四捨五入(注50は切り捨て)
```
**data type**
| Type | desc |
| ---- | ---- |
| np.uint8 | 画像で使う |
| np.int32 | MLで使う､Javaデフォ |
| np.int64 | npデフォ |
| np.float32 | MLで使う |
| np.float64 | npデフォ､溢れやすい |
| np.complex64 | float32+虚数 |
| np.bool | 実は1byte |

```
# Boolean mask
配列ごとの条件式は､index代わりにできる
arr[arr>=5] = 5 #5以上を5にする
arr[np.isin(arr, arr_c, invert=True)]=0 #arr_cに存在しない値を0にする

# Cast(データ型の変更)
print(arr.dtype)
arr.astype(np.float32) #演算前にメモリ溢れ対策
arr_boolean.astype(np.uint8)*5 #条件式に四則演算
arr.astype(int32) #1.5->1(切り捨て) -1.5->-1(切り上げ)
```
## numpy(2次元)
```
# 操作
## 結合
x1, x2 = np.array([1,2,3]), np.array([4,5,6])
x = np.concatenate([x1, x2]) #列に横追加
x = np.stack([x1, x2]) #同じshapeで行追加(axis=1なら列方向に追加､paddingはしてくれない)
x = np.vstack([x, x2]) #行追加(同じ列)

## 演算
y = np.array([[1,2,3],[4,5,6]])
y+2 # [[3,4,5],[6,7,8]]
np.dot(A, B) #行列積
## スライス
y = np.array([[1,2,3],[4,5,6],[7,8,9]])
y[1] #行取り出し [4,5,6]
y[:, 1] #列取り出し [2,5,8]
```
## numpyとりあえず
```
# 集約関数(配列を処理して任意の結果を返す関数)
np.sum(), np.prod, np.mean, np.median, len # 和､積､平均､標準偏差､中央値､要素数
np.max, np.min, np.argmax, np.argsort # 最大値､最小値､最大値idx, 昇順sortしたidx(降順は[::-1]で取得)
np.sum(A, axis=1) #0だと列ごと､1だと行ごと
# 便利な集約関数でない関数
np.sin, np.exp, np.log, np.abs, np.sqrt, np.maximum, np.minimum
np.sort, np.sort[::-1] #昇順sort, 降順sort
## 通常の関数は配列構造を維持して返す､numpyでは通常の関数にも配列を渡せる

# 検索
purin_idx = np.where(pokemon["names"]=='プリン')[0]
```

## dict
```
## defaultdict
### 初期化
from collections import defaultdict
d = deaultdict(int) # keyerr避けにdictの代わりに
d = deaultdict(lambda:5) # 初期値は関数指定
d = deaultdict(lambda:deaultdict(list))

### 操作
d['key'] == d.get('key')
d = dict(d) # keycheckや存在確認欲しかったらdictへ

for k in d.keys():
for v in d.values():
for k, v in d.items():

### sort
d_sorted_tuple = sorted(d, reverse=True, key=lambda x: x[1])  # valueで降順ソートでtuple化
d_sorted = dict(sorted(d, key=lambda x:x[0])) # keyで昇順ソートしてdict化
```

## その他(未整理)
```
# 進数､論理和/論理積/排他的論理積
bin(n), oct(n), hex(n) # 9=0b101, 2進数､8進数､16進数
int('101', 2) # 2進数⇒10進数
np.base_repr(n, base=9) #10進数⇒9進数

0b101>>2 # 右bitシフト 0b1=1
0b101<<2 # 左bitシフト 0b10100=20
1&9 # AND 001&101=001
1|9 # OR 001|101=101
1^9 # XOR 001|101=100 x|y=z x|z=y

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
## intはlongなのでoverflowしない(上限なし)
## floatはoverflowする(64bit)

# 正確な計算
## 16桁未満はint/floatでおk､問題は16桁以上
from fractions import Fraction
x = Fraction('1')/Fraction('3')
print('{:.9f}'.format(float(x))) #小数点9桁切り捨て

# 整数化処理
round(x) # 四捨五入
A//B # 整数切り捨て
math.ceil(A/B), -(-1*A//B) # 整数切り上げ

# 累乗とmod
a ** b # これでもいいが､powが10倍はやい
pow(a,b,c) # a**b%c
## 足し算､引き算､掛け算は､適宜modしてよい
30%3 == (10%3+20%3)%3 # 最後にmodするなら､初めからmodして良いし早い
## しかし､割り算は､割り算の替わりに､割る数の逆元を掛ける必要がある
30/7%mod != 30%mod --/7-- %mod %mod
inv = pow(7, -1, mod)
30/7%mod == 30%mod --*inv-- %mod %mod

# 階乗
math.factorial(n)

# 最大公約数/最小公倍数 3.9-
math.gcd(a,b)
math.lcm(a,b)


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

# 正規表現
re.match(r'([a-z]+)@([a-z]+)\.com', str1)
# [start-end]+は､1文字以上繰り返される場合にマッチ
https://note.nkmk.me/python-re-match-search-findall-etc/

まだやってないやつ
30-32
34
42 std::set https://qiita.com/tatyam/items/492c70ac4c955c055602

```

# Jupyter Tips

## bash
ワンライナーなら!､複数行なら##bashを宣言する
```
!ls
##bash
```