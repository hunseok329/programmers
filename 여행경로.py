from collections import deque

def solution(tickets):
    graph = {}
    
    for x, y in tickets:
        if x not in graph:
            graph[x] = [y]
        else:
            graph[x].append(y)
            graph[x].sort()
            
    stack = ['ICN']
    path = []
    
    while len(stack) > 0:
        top = stack[-1]

        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[top].pop(0))
    return path[::-1]