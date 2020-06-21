def solution(n):
    result = sorted(str(n))
    return int("".join(result[::-1]))
