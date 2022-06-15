# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    # Bracketsより簡単なのでおしまい
    # 1種類のカッコしかないのでスタックすらいらずに，カウントするだけ
    cnt = 0
    for c in S:
        if c == "(": 
            cnt += 1
        else:
            if cnt == 0: return 0 
            cnt -= 1
    # end of for 

    return 1 if cnt == 0 else 0
# end of func