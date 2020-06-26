def solution(N, stages):
    length = len(stages)
    result = []
    for i in range(1, N+1):
        if length != 0:
            result.append([i, stages.count(i)/length])
            length -= stages.count(i)
        else:
            result.append([i, 0])
    return [num[0] for num in sorted(result, key=lambda x: x[1], reverse=True)]
