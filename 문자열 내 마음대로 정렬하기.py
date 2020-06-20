def solution(strings, n):
    for i in range(len(strings)-1):
        for j in range(1, len(strings)-i):
            if ord(strings[j-1][n]) == ord(strings[j][n]):
                if strings[j-1] > strings[j]:
                    strings[j-1], strings[j] = strings[j], strings[j-1]
                    continue
                else:
                    continue
            if ord(strings[j-1][n]) > ord(strings[j][n]):
                strings[j-1], strings[j] = strings[j], strings[j-1]
    return strings
