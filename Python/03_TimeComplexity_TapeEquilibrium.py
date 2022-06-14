# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    left = A[0]
    right = sum(A) - A[0]
    ans = abs(left - right)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        ans = min(ans, abs(left - right))

    return ans 
# end of func