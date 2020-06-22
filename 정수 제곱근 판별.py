import math


def solution(n):
    num = int(math.sqrt(n))
    if math.pow(num, 2) == n:
        return math.pow(num+1, 2)
    else:
        return -1
