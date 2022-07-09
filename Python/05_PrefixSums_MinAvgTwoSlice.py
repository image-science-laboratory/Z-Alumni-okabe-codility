# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # ごちゃごちゃ書いてるけどもっと簡単明快な解法ありました
    # 2個以上連続する要素の平均が最小になるようにしたい
    # → 2個 or 3個の連続する要素だけを見れば良い
    # 2個の要素でスライスしたとき，n/2 個の各スライスについて平均を出し，その最小をamin, 最大をamaxとする．
    # 4個の要素でスライスしたとき，n/4 個の各スライスについて平均を出し，その最小をbmin, 最大をbmaxとする．
    # このとき必ず amin <= bmin <= bmax <= amax が成り立つ．
    # 3個と6個についても同じ事が言える．
    # 2個と3個については言えないパターンがあるので別々に調べる．
    # 例: 5 0 5 0 0 0 0 .... みたいな配列だと3個のスライスが最大(マイナスならば最小)になる．
    # 4個以上については，2個のスライスと3個のスライスの足し合わせで表現されて，スライス同士を足し合わせた場合は上で言ってる様に最大最小のパターンは存在しない
    
    
    
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
    # 累積和は [) の半開区間で考えるのでrightの値に注意(PDFは[]の閉区間で考えてそう)
    while left < n - 1:
        ave = (prefix[right] - prefix[left]) / (right - left)
        if minAve > ave:
            minAve = ave 
            minInd = left 
        
        # 1. 右端に到達したら左側を無条件で縮み続けさせる(終了処理)
        
        # 2. 要素3以上の範囲の時に，次の要素がaveよりも高い場合
        # 　→ 現在のrightに至るまでの最小が出せてるのでひたすら左を縮める
        #     (縮めることで更に小さい範囲を見つけられるかも)
        
        # 　→ 0 <= A < B < C < N のようなA,B,Cがあるとき，
        # 　→ [A..B)と[B..C)の範囲の平均を考える
        # 　→ mean[A..B) > mean[B..C) ならば mean[A..B) > mean[A..C)
        #　 → つまり，範囲[A..B)は範囲[B..C)を取り込む価値がある(取り込むと平均が下がるので)
        # 　→ 逆に mean[A..B) < mean[B..C) ならば mean[A..B) < mean[A..C)
        # 　→ よって，[A..B) は [B..C) を取り込まない(取り込むと平均が上がるので，だったらやり直したほうが良い)
        
        #   → このとき，[0..B) の範囲で最適解が出ているので，新たに[B..N)の範囲で最適解を探しに行く(これを繰り返す)
        # 　→ 良い感じの範囲に不要な範囲が混ざることを避けつつ貪欲みたいにしてる
        if right == n or right - left > 2 and A[right] >= ave:
            left += 1
        else:
            right += 1
    # end of while 

    return minInd
# end of func

