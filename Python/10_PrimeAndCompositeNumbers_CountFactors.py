# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math 

def solution(N):
    # write your code in Python 3.6
    
    # √(N)まで見ればOK (PDF参照)
    # a < √(N) かつ N % a == 0 ならば
    # (N / a) > √(N) かつ N % (N / a) == 0 が成り立つ． 
    ans = 0 # 1はすべての約数
    sqn = math.sqrt(N) 
    sqni = int(rtn)

    for i in range(1, sqni + 1):
        if N % i != 0: continue 
        ans += 1
        if i != sqn: ans += 1

    return ans    
# end of func
    
