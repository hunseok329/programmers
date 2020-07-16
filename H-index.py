def solution(citations):
    num = max(citations)
    for i in range(num, -1, -1):
        if sum(1 for x in citations if x >= i) >= i:
            break
    return i
