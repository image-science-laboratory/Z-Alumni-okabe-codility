# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# ユークリッド互除法で最大公約数
# pythonだとmath.gcd()とかあるけどね
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

def solution(N, M):
    # write your code in Python 3.6
    
    # (M * a) mod N はすべてGCD(M, N)の倍数である
    # GCD(M, N) * a <= N となるaをすべて列挙すれば良いことになる
    return N // gcd(N, M)
# end of func