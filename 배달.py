from collections import deque

def solution(N, road, K):
    visit = [0] * (N+1)
    graph = {}
    count = 0
    
    for r in road:
        if r[0] not in graph:
            graph[r[0]] = [r[1:]]
        else:
            graph[r[0]].append(r[1:])
        if r[1] not in graph:
            graph[r[1]] = [[r[0], r[-1]]]
        else:
            graph[r[1]].append([r[0], r[-1]])
            
    q = deque([1])
    while q:
        x = q.popleft()
        for b, t in graph[x]:
            if b == 1:
                continue
            time = visit[x] + t
            if visit[b] == 0:
                visit[b] = time
                q.append(b)
            else:
                if visit[b] > time:
                    visit[b] = time                    
                    q.append(b)
    for i in range(1, N+1):
        if visit[i] <= K:
            count += 1
    return count