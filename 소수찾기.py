def solution(n):
    answer = [True] * n
    max_length = int(n ** 0.5)
    for i in range(2, max_length+1):
        if answer[i-1]:
            for j in range(i+i, n+1, i):
                answer[j-1] = False
    return len([x for x in range(2, n+1) if answer[x-1]])
