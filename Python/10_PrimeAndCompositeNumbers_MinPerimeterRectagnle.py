# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N):
    # write your code in Python 3.6
    
    # 10-1 CountFactors と同じ
    # 約数を列挙して外周を計算するだけ
    ans = float("inf")
    sqn = math.sqrt(N)  
    sqni = int(sqn) 

    for i in range(1, sqni + 1):
        if N % i != 0: continue  
        d = (i * 2) + (N / i * 2) 
        ans = min(ans, d)  
    
    return int(ans)    
# end of func
