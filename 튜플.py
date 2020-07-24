def solution(s):
    s = s[1:-2]
    s = s.replace('},', '')
    s = sorted(s.split('{'), key=lambda x: len(x))
    result = []
    for i in range(len(s)):
        if ',' in s[i]:
            s[i] = s[i].split(',')
        elif s[i] != '':
            s[i] = [s[i]]
    for j in range(1, len(s)):
        for w in range(j):
            if s[j][w] not in result:
                result.append(s[j][w])
    return list(map(int, result))
