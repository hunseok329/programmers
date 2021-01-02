def incoding(music):
    music = music.replace('A#', 'a')
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    return music

def cutTime(musicTime):
    start_time = list(map(int, musicTime[0].split(':')))
    end_time = list(map(int, musicTime[1].split(':')))
    
    hour = end_time[0] - start_time[0]
    if hour != 0:
        end_time[1] += hour * 60
    return end_time[1] - start_time[1]
        
    

def solution(m, musicinfos):
    m = incoding(m)
    arr = []
    num = 0
    for music in musicinfos:
        music = incoding(music)
        music = music.split(',')
        time = cutTime(music[:2])
        
        if len(music[3]) >= time:
            music[3] = music[3][:time]
        else:
            div = time // len(music[3])
            mod = time % len(music[3])
            
            music[3] *= div
            music[3] += music[3][:mod]
        if m in music[3]:
            arr.append([num, time, music[2]])
        num += 1
            
    if len(arr):
        arr.sort(key=lambda x : (-x[1], x[0]))
        return arr[0][2]
    return '(None)'