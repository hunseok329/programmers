def solution(survey, choices):
    maps = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for idx, val in enumerate(choices):
        if val < 4: # 비동의 선택지
            maps_idx = survey[idx][0]
            maps[maps_idx] += (4 - val)
        else: # 동의 선택지
            maps_idx = survey[idx][1]
            maps[maps_idx] += (val - 4)
    answer = ""
    
    for x in ["RT", "CF", "JM", "AN"]:
        if maps[x[0]] == maps[x[1]]:
            answer += x[0]
        elif maps[x[0]] < maps[x[1]]:
            answer += x[1]
        else:
            answer += x[0]
            
    return answer
            