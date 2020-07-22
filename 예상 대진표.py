def solution(n, a, b):
    while n != 1:
        n = n // 2
        if (a <= n and b <= n):
            continue
        elif (a > n and b > n):
            a -= n
            b -= n
            continue
        else:
            n = n*2
            num = 0
            while n != 1:
                n = n // 2
                num += 1
            return num
