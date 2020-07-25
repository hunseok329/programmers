def solution(n):
    count = 0
    for i in range(1, n):
        s = 0
        for j in range(i, n):
            s += j
            if s == n:
                count += 1
            elif s > n:
                break
    return count + 1
