from collections import deque

def solution(n, edge):
    graph = {}
    for a, b in edge:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    visit = [0] * (len(graph) + 1)
    visit[1] = 1
    
    def bfs(root):
        q = deque([root])
        
        while q:
            v = q.popleft()
            for x in graph[v]:
                if visit[x] == 0:
                    q.append(x)
                    visit[x] = visit[v] + 1
    bfs(1)
    result = max(visit)
    return visit.count(result)