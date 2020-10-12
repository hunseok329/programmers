def solution(operations):
    result = []
    p = [x.split() for x in operations]
    for s in p:
        if s[0] == 'I':
            result.append(int(s[-1]))
        else:
            if result:
                if s[-1] == '1':
                    del result[-1]
                else:
                    del result[0]
            else:
                continue
        result.sort()
    return [max(result), min(result)] if result else [0, 0]
