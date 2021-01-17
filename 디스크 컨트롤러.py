import heapq
def solution(jobs):
    count, last, result = 0, -1, 0
    
    heap = []
    length = len(jobs)
    time = jobs[0][0]
    jobs.sort()
    while count < length:
        for s, e in jobs:
            if last < s <= time:
                heapq.heappush(heap, (e, s))
        
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            result += (time-start)
        else:
            time += 1
    return result//length