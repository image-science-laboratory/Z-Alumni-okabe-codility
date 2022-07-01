# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # -- 前提となる性質 -- 大体あってると思うけどいい感じに証明してください
    # 集合の数学的な書き方がよくわからないので，n(A) で要素数を出していると読み替えてください
    # Aの最頻値がa かつ n(a∈A) > n(A) / 2 のとき，
    # left = (a_0, .. , a_s) と right = (a_(s+1), .. , a_(N-1)) のどちらかの最頻値は必ずaになる
    # → leftとrightそれぞれの集合の最頻値が同じ値になるとき，その値は必ずAの最頻値aと一致する
    # また，n(a∈A) < n(A) / 2 のとき，
    # leftとrightそれぞれの最頻値 s1,s2 が s1=s2 かつ n(s1) > S/2 かつ n(s2) > (N-S)/2 になることはない
    # → Aの最頻値aが過半数を取っていなければ，leftとrightの各最頻値が一致してなおかつ各集合の過半数を取ることはない
    
    # 0 <= i < N の各iについての最頻値はO(N)でわかる(PDF見ると多分そんな感じ)
    # 左半分はこの方法で毎回O(1)で最頻値を更新しながら見る
    # 右半分は予め 0 < i < N の範囲で (i..N) について最頻値を出しておく O(N)
    # あとは毎回比べていくだけ
    # 前処理O(N)，線形探索O(N)なので O(N + N)でOK
    # 最頻値をどうのこうのする処理が非常に煩雑で下手くそなのでもっときれいに作ってください
    n = len(A)
    rightStack = []
    rightStackCount = {}
    rightStackLog = [None] * n  
    for i in range(n - 1, -1, -1):
        a = A[i] 
        if a in rightStackCount: rightStackCount[a] += 1
        else: rightStackCount[a] = 1
        
        if len(rightStack) == 0:
            if rightStackCount[a] <= (n - i) / 2: continue   
            rightStack.append(a)
        elif rightStack[-1] == a:   # 同じ値が入っている → 値が入っている時点でそいつは過半数
            rightStack.append(a) 
        else:
            rightStack.pop() 
        # end of if 

        if len(rightStack) > 0: rightStackLog[i] = rightStack[-1]
    # end of for 

    # 左半分も見ながら比較していく
    ans = 0
    leftStack = []
    leftStackCount = {}
    for i in range(1, n):
        a = A[i - 1]
        if a in leftStackCount: leftStackCount[a] += 1
        else: leftStackCount[a] = 1

        if len(leftStack) == 0:
            if leftStackCount[a] <= i / 2: continue   
            leftStack.append(a) 
        elif leftStack[-1] == a:
            leftStack.append(a) 
        else:
            leftStack.pop() 
        # end of if 

        if len(leftStack) > 0 and leftStack[-1] == rightStackLog[i]:
            ans += 1
    # end of for
    return ans 
# end of func
