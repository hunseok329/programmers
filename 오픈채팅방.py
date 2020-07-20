def solution(record):
    for num in range(len(record)):
        record[num] = record[num].split(' ')
    c = {}
    result = []
    for i in range(len(record)):
        if record[i][0] == 'Change' or record[i][0] == 'Enter':
            c[record[i][1]] = record[i][2]
        if record[i][0] == 'Enter':
            record[i][0] = '님이 들어왔습니다.'
            result.append(record[i][:2])
        elif record[i][0] == 'Leave':
            record[i][0] = '님이 나갔습니다.'
            result.append(record[i][:2])
    for j in range(len(result)):
        result[j][-1] = c[result[j][-1]]
        result[j].reverse()
        result[j] = ''.join(result[j])
    return result
