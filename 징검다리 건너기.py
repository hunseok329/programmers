def check(n, stone, k):
    count = 0
    for x in range(len(stone)):
        if stone[x] <= n:
            count += 1
        else:
            count = 0
        if count == k:
            return True
    return False

def solution(stones, k):
    start = 1
    end = max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        
        if check(mid, stones, k):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans