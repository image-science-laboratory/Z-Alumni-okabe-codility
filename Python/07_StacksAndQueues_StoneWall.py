# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    
    # 上がる時は必ずブロックが必要
    # 下がる時はすでにその高さのブロックを使っていれば必要ない(横長にすると良い)
    # (0..i)の範囲で出現したかどうかではないので注意(dictではできない)
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
        else:
            while len(stack) > 0 and stack[-1] > h:
                stack.pop()

            # スタックがなくなるか，hと同じ高さがスタックになければブロック追加
            if len(stack) == 0 or stack[-1] < h: 
                ans += 1 
                stack.append(h)  

            # 同じ高さのブロックがあれば何もしなくて良い
    # end of for

    return ans 
# end of for
        
