# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)


    # 各要素の出現回数をカウント
    dic = {}
    for a in A:
        if a in dic: dic[a] += 1
        else: dic[a] = 1

    # エラトステネスの篩みたいな感じで
    # aの倍数にaの出現回数を足してく
    # よって， 0 <= e < (2n + 2) のとき eratos[e] は
    # e % a == 0 となる a∈A の個数を表す
		# エラトステネスの篩の計算量が O(Nloglog(N))なので，
		# それより軽いこのアルゴリズムは大丈夫
    eratos = [0] * (2 *  n + 2) # 1 <= a <= n のため
    for key, value in dic.items():
        k = key
        while k < len(eratos):
            eratos[k] += value    
            k += key
    # end of for

    ans = [0] * n
    for i in range(n):
        ans[i] = n - eratos[A[i]]

    return ans 
# end of func
    


 