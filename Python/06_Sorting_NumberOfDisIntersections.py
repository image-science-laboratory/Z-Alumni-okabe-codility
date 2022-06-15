# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # 基本的な考え方は Lesson5-1 PassingCars と同じ
    # 円の左端が来たらカウントをプラス
    # 円の右端が来たらカウントを一つ減らしてansに現在のカウントをプラス
    # 左端と右端のチェックは小数点以下ですると便利(フラグとかの他の変数を用意しなくて良い)
    n = len(A)
    arr = [None] * (n * 2)
    for i in range(n):
        arr[i * 2] = i - A[i]
        arr[i * 2 + 1] = i + A[i] + 0.5
    
    arr.sort() 
    ans = 0 
    cnt = 0
    for a in arr:
        if a % 1 == 0:
            cnt += 1
        else:
            cnt -= 1
            ans += cnt 
    # end of for
    
    return ans if ans <= 10000000 else -1
# end of func

