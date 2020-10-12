def solution(n):
    p = [0 for _ in range(n)]
    p[0] = 1
    p[1] = 2
    for i in range(2, n):
        p[i] = (p[i-1] + p[i-2]) % 1000000007
    return p[-1]
