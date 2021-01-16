from collections import deque

def solution(n, computers):
    visited = [0] * n
    dq = deque()
    answer = 0
    while 0 in visited:
        dq.append(visited.index(0))
        
        while dq:
            x = dq.popleft()
            visited[x] = 1
            
            for i in range(n):
                if computers[x][i] == 1 and visited[i] == 0:
                    dq.append(i)
        answer += 1
    return answer