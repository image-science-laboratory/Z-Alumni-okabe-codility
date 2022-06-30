# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    ans = -1 * (10 ** 10)
    sum_ = 0
    left = 0
    right = 0

		# 合計が0以上の間は範囲を広げる
		# 0以下になったらその範囲をそれ以上探索する必要はない
    while right < len(A):
        sum_ += A[right]
        ans = max(ans, sum_)

        if sum_ < 0: 
            left = right 
            sum_ = 0
    
        right += 1
    # end of while 
    return ans
# end of func
