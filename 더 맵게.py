import heapq as hq


def solution(scoville, K):
    count = 0
    hq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        fir = hq.heappop(scoville)
        sec = hq.heappop(scoville)
        if sec == 0:
            hq.heappush(scoville, fir)
        else:
            mix = fir + (sec * 2)
            hq.heappush(scoville, mix)
        count += 1
    return count if min(scoville) > K else -1
