# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        if a in dic: dic[a] += 1
        else: dic[a] = 1
    # end of for

    items = dic.items() 
    items = sorted(items, key=lambda x: x[1], reverse=True)
    #print(items)
    if len(items) == 0 or items[0][1] <= len(A) / 2: return -1 
    else: return A.index(items[0][0])
# end of func