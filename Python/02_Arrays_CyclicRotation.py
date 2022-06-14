# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    n = len(A) 
    ans = [0] * n   
    for i in range(n):
        ans[(i + K) % n] = A[i]
    return ans
# end of func