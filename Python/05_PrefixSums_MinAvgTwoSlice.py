# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # とりあえず累積和
    n = len(A)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]

    # 尺取法みたいな感じで貪欲に伸び縮みしながら探索
    minAve = 10 ** 10
    minInd = 1
    left = 0
    right = 2
    while left < n - 1:
        ave = (prefix[right] - prefix[left]) / (right - left)
        if minAve > ave:
            minAve = ave 
            minInd = left 
        
        # 1. 右端に到達したら左側を無条件で縮み続けさせる
        # 2. 要素3以上の範囲の時に，範囲右側の値が平均よりも高い 
        # 　→ 現在のrightに至るまでの最小が出せてるのでひたすら左を縮める
        # 　→ 0 <= A < B < C < N のようなA,B,Cがあるとき，
        # 　→ (A, B)と(B, C)の範囲の平均を考える
        # 　→ (A, B) > (B, C)ならば (A, B) > (A, C)
        #　 → つまり，範囲(A, B)は範囲(B, C)を取り込む価値がある(取り込むと平均が下がる)
        # 　→ (A, B) < (B, C)ならば (A, B) < (A, C)
        # 　→ 逆に，(B, C)の平均が大きければ(A, B)は(B, C)を取り込まない(一つの範囲としてみなさない)
        # 　→ この方法ではこんな感じで配列の一部分を更に(A, B, C)のような要素に切り分けて，
        # 　→ 良い感じの範囲に不要な範囲が混ざることを避けつつ貪欲みたいにしてる
        if right == n or right - left > 2 and A[right] >= ave:
            left += 1
        else:
            right += 1
    # end of while 

    return minInd
# end of func

