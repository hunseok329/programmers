from math import factorial

def solution(n, k):
    num_list  = [num for num in range(1, n+1)]
    result = []
    
    while n != 0:
        n -= 1
        div, mod = divmod(k, factorial(n))
        k = mod
        if not mod : div -= 1
        result.append(num_list.pop(div))
    return result