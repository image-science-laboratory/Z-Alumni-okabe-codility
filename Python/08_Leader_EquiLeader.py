# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # -- 前提となる性質 -- 誰か証明してくれ
    # Aの最頻値がaで，なおかつaの個数がlen(A)の半分より多いとき，
    # (0..S) と (S+1..N-1) のどちらかの最頻値は必ずaになる
    # → 両方の最頻値が同じになるのは， (0..S) と (S+1..N-1)の両方の最頻値がaの時のみ
    # また，aの個数がlen(A)の半分以下の場合，
    # (0..S) と (S+1..N-1)の最頻値 s1, s2が s1=s2 かつ n(s1)>S/2 かつ n(s2)>(N-S)/2になることはない
    
    # 0 <= i < N の各iについての最頻値はO(N)でわかる(PDF見ると多分そんな感じ)
    # 左半分はこの方法で毎回O(1)で最頻値を更新しながら見る
    # 右半分は予め各iについての最頻値を出しておく O(N)
    # あとは毎回比べていくだけ
    # 前処理O(N)，線形探索O(N)なので O(N + N)でOK
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
