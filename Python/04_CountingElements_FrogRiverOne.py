# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    dic = {}
    for i in range(len(A)):
        dic[A[i]] = True 
        if len(dic) >= X: return i
    
    return -1
# end of func