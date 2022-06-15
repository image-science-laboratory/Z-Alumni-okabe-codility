# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    # pythonはlistでスタックとキューを作れる(ちゃんとO(1)で動くはず)
    dic = {}
    dic["("] = 0; dic[")"] = 0.5
    dic["{"] = 1; dic["}"] = 1.5
    dic["["] = 2; dic["]"] = 2.5
    stack = []

    for c in S:
        # 左側ならpushするだけ
        if dic[c] % 1 == 0: 
            stack.append(c) 

        # 右側の場合，要素数0か非対応のカッコがくるとだめ
        # それ以外はpopするだけ
        else:
            if len(stack) == 0: return 0
            pop = stack.pop()
            if dic[pop] != int(dic[c]): return 0
    # end of for

    # 余計なものが残ってなければOK ( { [ が多いと残る
    return 1 if len(stack) == 0 else 0
# end of func


