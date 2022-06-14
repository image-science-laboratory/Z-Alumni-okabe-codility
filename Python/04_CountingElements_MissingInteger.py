# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        if a > 0: dic[a] = True  
    
    for i in range(1, 10 ** 10):
        if i not in dic: return i 
# end of func
