def solution(n, costs):
    costs = sorted(costs, key=lambda x : x[-1])
    graph = {costs[0][0]}
    total = 0
    
    while len(graph) < n:
        for a,b,c in costs:
            if a in graph and b in graph:
                continue
            if a in graph or b in graph:
                graph.update([a, b])
                total += c
                break
    return total