def cut_time(l):
    temp = l.split()
    min_time = 0.001
    time = list(map(float, temp[1].split(':')))
    for i in range(1, len(time)):
        time[i] += time[i-1] * 60
    start_time = time[-1] - float(temp[-1][:-1]) + min_time
    end_time = time[-1]
    return [start_time, end_time]
        
def solution(lines):
    traffic = []
    result = 0
    for x in lines:
        traffic.append(cut_time(x))
    traffic = sorted(traffic, key=lambda x : x[1])

    for t in traffic:
        start = t[0]
        end = t[1]
        count = 0
        for i in traffic:
            if i[1] >= end and i[0] < end+1:
                count += 1
        result = max(result, count)
    return result