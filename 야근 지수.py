import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    for i in range(n):
        p = heapq.heappop(works)
        if p >= 0:
            break
        p += 1
        heapq.heappush(works, p)
    result = 0
    for i in works:
        result += i**2
    return result
