def solution(n):
    result = n+1
    a = bin(n)[2:].count('1')
    while True:
        b = bin(result)[2:].count('1')
        if a == b:
            return result
        result += 1
