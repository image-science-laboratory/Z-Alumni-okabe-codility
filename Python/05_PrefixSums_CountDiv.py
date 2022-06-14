# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A, B, K):
    # write your code in Python 3.6
    return (math.floor(B / K) - math.ceil(A / K)) + 1
# end of func