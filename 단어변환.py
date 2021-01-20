from collections import deque
def solution(begin, target, words):
    queue = deque([[begin]])
    visited = [True] * len(words)
    count = 0
    if target not in words:
        return 0
    while True:
        word = queue.popleft()
        temp = []  
        for w in word:
            for i in range(len(words)):
                if visited[i]:
                    diff = 0
                    for x in range(len(w)):
                        if w[x] != words[i][x]:
                            diff+= 1
                    if diff == 1:
                        temp.append(words[i])
                        visited[i] = False
        queue.append(temp)
        count += 1
        if target in temp:
            return count