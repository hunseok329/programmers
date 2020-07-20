import heapq


def solution(stock, dates, supplies, k):
    count = 0
    start = 0
    check = []
    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(check, (-supplies[i], supplies[i]))
                start = i + 1
            else:
                break
        stock += heapq.heappop(check)[1]
        count += 1
    return count
