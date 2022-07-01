# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    
    # 左から順に見ていって，上がる時は必ずブロックが必要
    
    # 下がる時はちょっと処理が面倒
    # a_(i-1) > a_i のように，i番目の要素で下がるとき
    # 0 <= j < i の範囲で a_j <= a_i を満たす最大の j を j_max とする
    # → つまり，現在見ているブロック以下の高さのやつの内，今まで探索した中で最後に出てきたやつが j_max
    # j_max <= k < i の範囲で a_k = a_i となるブロックがあれば a_i のために新たにブロックを用意する必要がない
    # → a_k のブロックを a_i まで右に横長に伸ばせば良い
    
    stack = []
    ans = 0
    for h in H:        
        # 上がる時はスタックに追加してカウントするだけ
        if len(stack) == 0 or stack[-1] < h:
            ans += 1
            stack.append(h)
        
        # 同じ時は何もしない
        elif stack[-1] == h:
            continue 
        
        # 下がる時はスタックに同じ高さがあれば新規ブロックは必要ない
        # j_max <= k < i の中に a_k = a_i となる k が1個以上存在する場合，
        # 最大の k を k_max とする．
        # そうすると， k_max .. i-1 の範囲の値は必要なくなるので消す
        # → a_(k_max) .. a_(i-1) は全て a_i よりも値が大きい → a_i より右側にブロックを伸ばせないので
        # この問題は条件を満たす要素の内，最後に出現するやつが大切だということが分かる (j_max とか k_max とか言ってるし)
        # → 最後に出現した要素を見ていくのはスタックが便利 (LIFO なので)
        else:
            while len(stack) > 0 and stack[-1] > h:
                stack.pop()

            # a_i と同じ高さがスタックになければブロック追加
            if len(stack) == 0 or stack[-1] < h: 
                ans += 1 
                stack.append(h)  

            # 同じ高さのブロックがあれば何もしなくて良い
    # end of for

    return ans 
# end of for
        
