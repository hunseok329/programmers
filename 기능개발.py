def solution(progresses, speeds):
    result = []
    while len(speeds) != 0:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        count = 0
        for num in progresses:
            if num >= 100:
                count += 1
            else:
                break
        if count != 0:
            result.append(count)
            progresses = progresses[count:]
            speeds = speeds[count:]
    return result
