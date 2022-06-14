# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6

		# N+1 のクエリのたびに counters=[0]*N をすると間に合わない(10**5個の初期化は遅い)
		# N+1 のクエリの時のその時のcountersの最大値を保存
		# <=N のクエリの時にcounters[i]とmaximumの大きい方を参照することでmaxcounter処理を実装(初期化せずに足し算だけで実装できる)
		# 一時的な最大値とmax counter処理の最大値を分けて考えることに注意
    maximum = 0
    tmpMax = 0
    counters = [0] * N
    for i in range(len(A)):
        a = A[i] - 1
        if a < N:
            counters[a] = max(counters[a], maximum) + 1 
            tmpMax = max(tmpMax, counters[a])
        else:
            maximum = tmpMax

		# 呼ばれていないcounterをmaximumに
    for i in range(N):
        counters[i] = max(counters[i], maximum)

    return counters
# end of func            



