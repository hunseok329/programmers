def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            temp = 0
            for w in range(4):
                if w != j and land[i-1][w] > temp:
                    temp = land[i-1][w]
            land[i][j] += temp
    return max(land[-1])
