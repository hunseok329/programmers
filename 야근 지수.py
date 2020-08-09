import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    for i in range(n):
        p = heapq.heappop(works)
        heapq.heappush(works, p+1)
    result = 0
    for i in works:
        result += i**2
    return result
