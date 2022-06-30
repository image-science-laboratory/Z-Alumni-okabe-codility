# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math 

def solution(A):
    # write your code in Python 3.6
    n = len(A)

    # n の約数を見つける(同じ要素数で分割するため)
    dic = {}
    sqn = int(math.sqrt(n)) + 1
    for i in range(1, sqn):
        if n % i != 0: continue   
        dic[i] = True 
        dic[n // i] = True

    factors = list(dic.keys())
    factors.sort()
   
    # ピークのインデックスを出す(Flagsと同じ)
    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]: peaks.append(i)
    pn = len(peaks)

    # factorsが各ブロックの要素数になり得る
    # 1が答えになることはないので2番目から探索する(peaksが連続することはありえない)
    for i in range(1, len(factors)):
        blockSize = factors[i]
        blockInd = 0
        blockNum = n // blockSize

        j = 0
        while j < pn:
            pj = peaks[j]
            left = blockInd * blockSize
            right = (blockInd + 1) * blockSize 

            # 範囲外ならそのブロックにピークがないので成り立たない
            if pj < left or right <= pj: break 

            # 範囲内の間ピークを読み進める
            # 同一のブロックに何個ピークがあっても良いが，
            # あくまでそのブロックのピークの有無だけなので1つあれば十分
            while left <= pj < right and j < pn - 1:
                j += 1
                pj = peaks[j]
            
            # このブロックにはピークがあったのでOK
            blockInd += 1
        # end of while

        # BlockIndがBlockNumと同じならすべてのブロックにピークが存在する
        if blockInd >= blockNum: return blockNum
    # end of for

    return 0
# end of func 



    
    