def solution(n, m):
    return [gcd(n, m), (n*m)/gcd(n, m)]


def gcd(a, b):
    while b > 0:
        r = b
        b = a % b
        a = r
    return a
