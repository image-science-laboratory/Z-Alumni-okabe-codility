# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        dic[a] = True  

    for i in range(1, len(A) + 1):
        if i not in dic: return 0
    
    return 1 
# end of func