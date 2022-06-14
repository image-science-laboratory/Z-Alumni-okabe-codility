# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        if a in dic: dic[a] += 1
        else: dic[a] = 1
    
    for key in dic.keys():
        if dic[key] % 2 == 1:
            return key 
# end of func
