from collections import deque

def bfs(node, target, maps, N, M):
    visited = [[0 for _ in range(N)] for _ in range(M)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([node])
    
    while q:
        x, y = q.popleft()    
        if [x, y] == target:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([nx, ny])
                    
    return -1
        

def solution(maps):
    answer = 0
    N, M = len(maps[0]), len(maps)
    
    for y in range(M):
        for x in range(N):
            if maps[y][x] == 'S':
                start = [x, y]
            elif maps[y][x] == 'E':
                end = [x, y]
            elif maps[y][x] == 'L':
                lever = [x, y]
                
    start_lever = bfs(start, lever, maps, N, M)
    if start_lever < 0:
        return -1
    lever_end = bfs(lever, end, maps, N, M)
    if lever_end < 0:
        return -1
    return start_lever + lever_end