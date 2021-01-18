def solution(genres, plays):
    music = {}
    musicRap = {}
    result = []
    for i in range(len(plays)):
        if genres[i] not in music:
            music[genres[i]] = [[plays[i], i]]
            musicRap[genres[i]] = plays[i]
        else:
            music[genres[i]].append([plays[i], i])
            music[genres[i]].sort(key=lambda x : (x[0], -x[1]))
            musicRap[genres[i]] += plays[i]
    
    res = sorted(musicRap.items(), key=lambda x : -x[-1])
    for x in res:
        temp = music[x[0]]
        if len(temp) >= 2:
            for y in temp[-2:][::-1]:
                result.append(y[-1])
        else:
            result.append(temp[-1][-1])
    return result