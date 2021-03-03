from collections import deque
def solution(maps):
    q = deque()
    q.append([0, 0])
    
    N, M = len(maps[0]), len(maps)
    
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append([ny, nx])
                elif maps[ny][nx] > maps[y][x] + 1 and maps[ny][nx] != 0:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append([ny, nx])
    if maps[-1][-1] != 1:
        return maps[-1][-1]
    else:
        return -1