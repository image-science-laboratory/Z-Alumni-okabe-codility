# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    dic = {}
    dic["A"] = 0
    dic["C"] = 1
    dic["G"] = 2
    dic["T"] = 3

    # ACGTそれぞれについての累積和を作れば各クエリに対してO(1)で求まる
    prefix = [[0] * (len(S) + 1) for i in range(4)]
    for i in range(1, len(S) + 1):
        for j in range(4):
            prefix[j][i] = prefix[j][i - 1]
        prefix[dic[S[i - 1]]][i] += 1
    # end of 

    # クエリ範囲で累積和の変化を見て最小を保存
    ans = [0] * len(P)
    for i in range(len(P)):
        p = P[i] 
        q = Q[i] + 1
        for j in range(4):
            if prefix[j][q] - prefix[j][p] > 0:
                ans[i] = j  + 1
                break 
        # end of for
    # end of for

    return ans 
# end of func


