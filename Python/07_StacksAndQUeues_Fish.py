# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    
    # 基本的な考え方は Lesson5-1 PassingCars と同じ
    # 上向きか下向きのどちらかをスタックに入れながら判定していく
    # 先頭から見ていく場合は下向きを保存すると楽
    ans = len(A)
    stack = []
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        #print(ans, a, b, stack)
        # 下向きのやつをスタックに入れていく
        if b == 1:
            stack.append(a)

        # 上向きのやつに出会ったら食べ合う
        else:
            while len(stack) > 0 and stack[-1] < a:
                ans -= 1
                stack.pop()

            # まだスタックが残っているなら，下向きの魚のほうが大きいのでaは食われる
            # 残っていないなら下向きの魚は全部食われたのでaは生還
            if len(stack) > 0: ans -= 1
    # end of for

    return ans 
# end of func
