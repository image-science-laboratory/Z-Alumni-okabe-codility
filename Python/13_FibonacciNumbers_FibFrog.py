# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
		# 向こう岸も葉っぱとして考えると楽
    A += [1]
    n = len(A)  

    # とりあえずフィボナッチを列挙する
    fibo = [1, 2]
    f = 3 
    while f <= n:
        fibo.append(f)
        f += fibo[-2]

    # 先頭から順にfiboで飛べるか見ていく
    # O(N * len(fibo))で，n=10^6のときでもlen(fibo)=29なので大丈夫
    flag = [0] * (n + 1)
    flag[0] = 1	# 最初の岸も葉っぱとして考えると楽
    for i in range(n + 1):
        # 葉っぱでない or 葉っぱだけど到達できないなら考えない
        if flag[i] == 0: continue   

        for f in fibo:
            if f + i >= n + 1 or A[f + i - 1] == 0: continue   

						# a番目の葉っぱに到達できる最小ジャンプ回数を記録していく
            if flag[f + i] == 0: flag[f + i] = flag[i] + 1
            else: flag[f + i] = min(flag[f + i], flag[i] + 1)
    
    return flag[-1] - 1 if flag[-1] > 0 else -1
# end of func
    
