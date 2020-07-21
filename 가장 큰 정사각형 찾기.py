def solution(board):
    length = 0
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            check = min(board[i][j:j+2] + board[i+1][j:j+2])
            if check != 0:
                board[i+1][j+1] = min(board[i][j:j+2]+board[i+1][j:j+1]) + 1
    for line in board:
        if max(line) > length:
            length = max(line)
    return length*length
