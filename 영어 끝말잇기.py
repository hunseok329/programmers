def solution(n, words):
    check = []
    num = 0
    while len(check) != len(words):
        if len(check) == 0:
            check.append(words[num])
        elif words[num] in check or check[-1][-1] != words[num][0]:
            return [(num % n)+1, (num//n)+1]
        else:
            check.append(words[num])
        num += 1
    return [0, 0]
