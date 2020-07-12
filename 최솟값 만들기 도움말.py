def solution(A, B):
    result = 0
    A.sort()
    B.sort(reverse=True)
    while A:
        result += (A.pop() * B.pop())
    return result
