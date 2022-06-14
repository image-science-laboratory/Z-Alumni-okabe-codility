# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    cnt = 0 
    ans = 0
    for a in A:
        if a == 0: cnt += 1
        else: ans += cnt   
    
    return ans if ans <= 10 ** 9 else -1
# end of func
            
