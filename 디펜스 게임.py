import heapq

def solution(n, k, enemy):
    heap = []
    
    # 무적권을 사용하여 무조건 막을 수 있는 기본 라운드 수
    for attack in enemy[:k]:
        heapq.heappush(heap, attack)
        
    # 힙을 이용하여 최소 디펜스 라운드 처리
    for idx in range(k, len(enemy)):
        heapq.heappush(heap, enemy[idx])
        n -= heapq.heappop(heap)
        
        if n < 0:
            return idx
    return len(enemy)
        
    
    return answer