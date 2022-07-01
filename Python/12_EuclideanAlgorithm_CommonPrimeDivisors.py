# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(a, b):
    if a * b == 0: return 0
    while a * b != 0:
        a, b = max(a, b), min(a, b)
        a = a % b 
    return int(max(a, b))
# end of func 

def lcm(a, b):
    if a * b == 0: return 0 
    return int(a * b / gcd(a, b))
# end of lcm

def solution(A, B):
    # write your code in Python 3.6
    n = len(A)
    ans = 0 
    for i in range(n):
        a, b = A[i], B[i]
        g = gcd(a, b) 

        # a=15, b=75 のように 共通のPrimedivisorを持つ場合
        # a = 3^1 * 5^1
        # b = 3^1 * 5^2 のように指数部分が異なるだけである
        # → 3^x * 5^y (0 <= x, y)で割り続ければ a,b は1になる
        # → GCD(a, GCD(a,b))のようにするとx,yをいい感じに決められる

        # a=10, b=30 のように共通のPrimeDivisorを持たない場合
        # a = 2^1 * 5^1
        # b = 2^3 * 5^1 * 3^1 のように底が異なるので
        # GCD(b, GCD(a, b))を繰り返しても a に 3 が含まれていないのでGCDに3の倍数が出ることはない
        # → 2^x * 5^y (0 <= x, y) で割り続けると 3^z みたいなのが残る
       
        gg = g
        while gg > 1:
            gg = gcd(a, g)
            a = a / gg  
    
        gg = g
        while gg > 1:
            gg = gcd(b, g)
            b = b / gg  

        if a * b == 1: ans += 1
    # end of for

    return ans
# end of func


