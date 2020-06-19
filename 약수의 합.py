def solution(n):
    answers = n
    for i in range(1, n//2+1):
        if n % i == 0:
            answers += i
    return answers
