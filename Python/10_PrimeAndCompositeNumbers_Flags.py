# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math 

def solution(A):
    # write your code in Python 3.6
    
    # とりあえずピークを出す
    n = len(A)   
    peaks = [] 

    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]: peaks.append(i)
    
    pn = len(peaks)
    if pn == 0: return 0 
    
    # K個のFlagを置くためにはK^2の距離が必要なため，答えの最大値はsqrt(N)
    # 二分探索で探していく O(NlogN) なので間に合う
    dic = {}
    left = 0
    right = n - 1
    while left <= right:
        mid = (right + left) // 2 
        res = check(pn, peaks, mid)
        dic[mid] = res
        if res == False:
            right = mid - 1
        else:
            left = mid + 1
    # end of while
    items = dic.items()
    items = sorted(items, key=lambda x: -x[0])
    for a, b in items:
        if b == True: return a
  
# end of func

def check(pn, peaks, k):
    cnt = 1 #最初のpeakには絶対フラグを立てるので
    prev = 0 
    current = 1
    while current < pn:
        if peaks[current] - peaks[prev] >= k: 
            cnt += 1
            prev = current 
        current += 1
    # end of while 
    return cnt >= k
# end of func
