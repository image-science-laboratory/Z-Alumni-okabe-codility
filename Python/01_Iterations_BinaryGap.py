# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    s = bin(N)[2:]
    cnt = 0 
    ans = 0
    for i in range(1, len(s)):
        if s[i] == "1":
            ans = max(ans, cnt)
            cnt = 0 
            continue
        cnt += 1
    return ans 
# end of func