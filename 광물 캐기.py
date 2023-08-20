def convert_value(mineral_list):
    result = 0
    for mineral in mineral_list:
        if mineral == "diamond": result += 25
        if mineral == "iron": result += 5
        if mineral == "stone": result += 1
    return result
            
def solution(picks, minerals):
    answer = 0
    mineral_fatigue = []
    
    for idx in range(0, len(minerals), 5):
        temp = minerals[idx:idx+5]
        mineral_fatigue.append([temp, convert_value(temp)])
    mineral_fatigue = sorted(mineral_fatigue[:sum(picks)], key=lambda x : -x[1])
    
    for mineral_list, fatigue in mineral_fatigue:
        length = len(mineral_list)
        if picks[0]:
            answer += length
            picks[0] -= 1
        elif picks[1]:
            diamond = mineral_list.count("diamond")
            answer += (length - diamond) + (diamond * 5)
            picks[1] -= 1
        elif picks[2]:
            diamond, iron = mineral_list.count("diamond"), mineral_list.count("iron")
            answer += (diamond * 25) + (iron * 5) + (length - (diamond + iron))
            picks[2] -= 1
    return answer