def solution(cacheSize, cities):
    result = 0
    cash = []
    for word in cities:
        if word.upper() in cash:
            cash.remove(word.upper())
            cash.append(word.upper())
            result += 1
        else:
            if cacheSize != 0:
                if len(cash) == cacheSize:
                    del cash[0]
                cash.append(word.upper())
            result += 5
    return result
