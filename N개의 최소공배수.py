import math


def solution(arr):
    while len(arr) != 1:
        A = arr.pop()
        B = arr.pop()
        arr.append(A*B//math.gcd(A, B))
    return arr[0]
