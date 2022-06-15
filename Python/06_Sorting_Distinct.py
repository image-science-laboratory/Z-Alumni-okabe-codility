# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        dic[a] = True 
    
    return len(dic)
# end of func
