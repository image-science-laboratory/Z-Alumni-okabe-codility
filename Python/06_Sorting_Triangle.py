# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    arr = sorted(A) 

    for i in range(2, len(arr)):
        if arr[i - 2] + arr[i - 1] > arr[i]: return 1 
    
    return 0
# end of func
