# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # 左から見た累積和と右から見た累積和を作る
    # このとき，0..X の範囲と Z..N-1 の範囲においてマイナスになる領域は選択しなければ良い
    # → 累積和を作るとに最低値を0にすることで実現できる(余計な部分を足さない)
    n = len(A)
    leftSum = [0] * n 
    for i in range(1, n):
        leftSum[i] = max(0, A[i] + leftSum[i - 1])
    
    rightSum = [0] * n 
    for i in range(n - 2,  -1, -1):
        rightSum[i] = max(0, A[i] + rightSum[i + 1])
    

    # Yを動かしながら見ていく
    # 0 < X < Y となるが，このときのXがどのような値であるかはわからなくて良い
    # 0 < X < Y の中で sum(A[X]..A[Y-1])が最大になるときの値がleftSum[Y-1]に入っている
    # Zも同様に Y < Z < N-1 となる最適なZがどのような値を取るかは分からないが
    # sum(A[Y+1]..A[Z])が最大となるときの値はrightSum[Y+1]でわかる
    ans = -1 * (10 ** 10)
    for i in range(1, n-1):
        ans = max(ans, leftSum[i-1] + rightSum[i+1])
    
    return ans 
# end of func
