# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # write your code in Python 3.6

	# 考え方を逆転させる
	# 通常 → どのように分割すれば合計を最小にできるか(分割する位置を探索する)
	# 今回 → 各ブロックの合計がS以下になるように好きな数で分割する
	#　　　　このとき，分割されたブロック数がK以下であればSは条件を満たす
	#　　　　条件を満たすSの内，最小のものを探す(分割する基準となる合計値を探索する)

	#　　　　Sが条件を満たしている場合，Sよりも大きい数値は必ず条件を満たす(調べる必要がない)
	#　　　　逆にSが条件を満たしていない場合，Sよりも小さい数値は必ず条件を満たさない(調べる必要がない)
	#　　　　↑なので二分探索で十分

    # 二分探索でK分割以下にできるSUMを探していく
    ans = 10 ** 12
    left = 0 
    right = 10 ** 12
    # 各要素最大10^6，要素数最大10^6, Log2(10^12)=39ぐらいなので Nlog(10^12) で間に合う

    while left <= right:
        mid = (left + right) // 2
        res = check(K, A, mid)
        if res == True:
            right = mid - 1
        else:
            left = mid + 1
  
        if res == True: ans = min(ans, mid)
    # end of while 

    return ans
# end of func


# ブロックの合計がS以下になるように分割した際に，
# ブロック数をK以下にできるか
def check(K, A, S):
    blockNum = 0
    sum_ = 0
    i = 0 
    while i < len(A):
        sum_ += A[i]
        if sum_ > S:
            sum_ = 0
            blockNum += 1
            if blockNum >= K: break 
            continue  
        
        i += 1
    # end of while
    return blockNum < K
# end of func
