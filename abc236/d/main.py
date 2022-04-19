import sys
def input():
    return sys.stdin.readline()[:-1]

a = []

def f(lis):
    """
    lis の中から2個とって、残りの要素について再帰する。
    lis の中味を2個ずつ分けたすべての組み合わせについて、
    a[i][j]のxorをとった値のリストを返す。

    ◆入力
    - lis : リスト。長さは偶数にすること。  例 : [0,1,4,5]
    ◆出力
    - sub_ans_list  : lisを2つずつ組にしたすべての場合について、A_ijのxorをとった値のリスト。
                        例 : [ a[0][1]^a[4][5], a[0][4]^a[1][5], a[0][5]^a[1][4] ]
    """
    ans_list = []

    # リスト先頭の人の番号
    pi = lis[0]
    for j in range(1,len(lis)):
        # リストj番目の人の番号
        pj = lis[j]
        # 先頭の人とj番目の人の相性
        bij = a[pi][pj]

        if len(lis)>2:
            # lisの中から、先頭とj番目を取り除いた小リストを作る。
            sub_list = lis[1:j]+lis[j+1:]

            # 小リストについて問題を解き、あり得るすべてのxorの値のリストを得る。
            sub_ans_list = f(sub_list)

            for sa in sub_ans_list:
                ans_list.append(sa^bij)
        else:
            ans_list.append(bij)

    return ans_list

def main():
    n = int(input())

    # aを行列の形に整形する。
    # 人xとyの相性は、(xとyを0-based indexで表記すると)
    # a[x][y]と表される。
    for i in range(2*n-1):
        a_row = list(map(int, input().split()))
        a_row = [0]*(i+1) + a_row
        a.append(a_row)

    # lis = [0,1,2, ... , 15]   # n=8の場合
    lis = list(range(2*n))

    # 問題を解く
    ans_list2 = f(lis)
    print(max(ans_list2))

if __name__ == '__main__':
    main()