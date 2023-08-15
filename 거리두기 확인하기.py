def bfs(place):
    for y, row in enumerate(place):
        for x, val in enumerate(row):
            if val != 'X':
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                cnt = 0

                for i in range(4):
                    mx = x + dx[i]
                    my = y + dy[i]

                    if 0 <= mx < 5 and 0 <= my < 5:
                        if val == 'O' and place[my][mx] == 'P': cnt += 1
                        if val == 'P' and place[my][mx] == 'P': return 0
                if cnt > 1: return 0
    return 1

def solution(places):
    return [bfs(place) for place in places]





def graph(place):
    for y, row in enumerate(place):
        for x, val in enumerate(row):
            if val == 'P':
                if x < 4 and row[x+1] == 'P':return 0
                if y < 4 and place[y+1][x] == 'P':return 0
                if x < 3 and row[x+2] == 'P' and row[x+1] == 'O':return 0
                if y < 3 and place[y+2][x] == 'P' and place[y+1][x] == 'O':return 0
                if x < 4 and 0 < y < 4:
                    if place[y-1][x+1] == 'P' and (place[y-1][x] == 'O' or row[x+1] == 'O'):return 0
                    if place[y+1][x+1] == 'P' and (place[y+1][x] == 'O' or row[x+1] == 'O'):return 0
    return 1

def solution(places):
    return [graph(place) for place in places]
        