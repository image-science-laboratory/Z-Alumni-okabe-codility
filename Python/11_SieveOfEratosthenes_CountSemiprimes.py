# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math 

def solution(N, P, Q):
    # write your code in Python 3.6

    # 自然数 a を割れる最小の素数を列挙する(自分自身はカウントしない)
    # → priFactor[a] == 0 ならば a は素数である
    priFactor = [0] * (N + 1)
    for i in range(2, int(math.sqrt(N)) + 1):
        if priFactor[i] != 0: continue  
        ii = i * i
        while ii <= N:
            if priFactor[ii] == 0: priFactor[ii] = i
            ii += i  
    # end of for

    # Nまでの半素数を列挙する
    semiPrimes = [0] * (N + 1)
    for i in range(2, N + 1):
        # 素数を約数に持たない → 素数である
        if priFactor[i] == 0: continue   

        # 自然数 a を割れる最小の素数 p があるとき
        # a / p の値が自身以外の約数を持たないなら半素数である
        # a = p * (a / p) かつ， p， a / p がともに素数なので a は２つの素数の積である
        if priFactor[i // priFactor[i]] == 0:
            semiPrimes[i] = 1
    # end of for 

    # 半素数の有無について累積和をとる
    # → 各クエリに対してO(1)でわかるようになる
    prefixSemiPrimes = [0] * (N + 1) 
    for i in range(1, N + 1):
        prefixSemiPrimes[i] = prefixSemiPrimes[i - 1] + semiPrimes[i]

    m = len(P)
    ans = [0] * m 
    for i in range(m):
        p, q = P[i], Q[i]
        # 累積和ではpのときに増えたかどうかがわからないのでsemiPrimes[p]で判別している
        ans[i] = prefixSemiPrimes[q] - prefixSemiPrimes[p] + semiPrimes[p]
    return ans   
# end of func


            
