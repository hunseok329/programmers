def find(board):
    data = []
    for y in range(len(board)-1):
        length = min(len(board[y]), len(board[y+1]))
        for x in range(length-1):
            if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                data.append((y, x))
                data.append((y, x+1))
                data.append((y+1, x))
                data.append((y+1, x+1))
    return data


def solution(m, n, board):
    board = list(map(lambda x: list(x), board))
    board = list(map(list, zip(*board[::-1])))
    count = 0
    while True:
        data = find(board)
        data = sorted(list(set(data)), reverse=True)
        count += len(data)
        if data:
            for y, x in data:
                del board[y][x]
        else:
            return count
