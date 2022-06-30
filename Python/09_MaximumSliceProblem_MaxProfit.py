# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) <= 1: return 0
    minimum = A[0]
    ans = 0

    for i in range(1, len(A)):
        tmp = A[i] - minimum 
        minimum = min(A[i], minimum)
        ans = max(tmp, ans)
    
    return ans
