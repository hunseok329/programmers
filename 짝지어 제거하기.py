def solution(s):
    result = []
    for word in s:
        if len(result) == 0:
            result.append(word)
        else:
            if result[-1] == word:
                result.pop()
            else:
                result.append(word)
    if len(result) == 0:
        return 1
    else:
        return 0
