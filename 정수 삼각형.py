def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])-1):
            if triangle[i][j] > triangle[i][j+1]:
                triangle[i-1][j] += triangle[i][j]
            else:
                triangle[i-1][j] += triangle[i][j+1]
    return triangle[0][0]


def solution(triangle):
    for high in range(len(triangle)-1, 0, -1):
        for row in range(len(triangle[high])-1):
            if triangle[high][row] < triangle[high][row+1]:
                triangle[high-1][row] += triangle[high][row+1]
            else:
                triangle[high-1][row] += triangle[high][row]
    return triangle[0][0]