def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            ret[x][N-1-y] = m[y][x]
    return ret   

def check(k, l):
    length = len(k)
    for y in range(length):
        for x in range(length):
            if (l[y][x] + k[y][x]) != 1:
                return False
    return True

def solution(key, lock):
    start = len(lock) - 1
    end = start + len(key)
    length = (start * 2) + len(key)
    
    ret = [[0]*(length) for _ in range(length)]
    
    for y in range(len(key)):
        for x in range(len(key)):
            ret[y+start][x+start] = key[y][x]
            
    for z in range(4):
        for y in range(end):
            for x in range(end):
                arr = []
                for i in range(len(lock)):
                    arr.append(ret[y+i][x:x+len(lock)])
                if check(arr, lock):
                    return True
        lock = rotate_90(lock)
    return False