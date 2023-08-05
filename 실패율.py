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


def solution(N, stages):
    answer = []
    
    users = len(stages)
    stage_num = {}
    
    for stage in range(1, N+1):
        stage_num[stage] = 0
        
    for stage in stages:
        if stage <= N:
            stage_num[stage] += 1
            
    for key, value in stage_num.items():
        if users:
            fail = ( value / users)
            answer.append([key, fail])
            users -= value
        else:
            answer.append([key, 0])
    return [x[0] for x in (sorted(answer, key=lambda x : (-x[1], x[0])))]



# 성능 개선
from collections import defaultdict

def solution(N, stages):
    answer = []
    users = len(stages)
    stage_num = defaultdict(int)
    
    for stage in stages:
        if stage <= N:
            stage_num[stage] += 1
    for idx in range(1, N + 1):
        value = stage_num[idx]
        if users:
            fail = ( value / users)
            answer.append([idx, fail])
            users -= value
        else:
            answer.append([idx, 0])
    return [x[0] for x in (sorted(answer, key=lambda x : (-x[1], x[0])))]
