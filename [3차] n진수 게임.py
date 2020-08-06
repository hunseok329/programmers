def division(num, n):
    p = '0123456789ABCDEF'
    s = ''
    while True:
        num, mod = divmod(num, n)
        s += p[mod]
        if num == 0:
            return s[::-1]


def solution(n, t, m, p):
    string = ''
    result = ''
    num = 0
    while len(string) < t*m:
        string += division(num, n)
        num += 1
    for i in range(p-1, t*m, m):
        result += string[i]
    return result
