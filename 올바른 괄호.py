def solution(s):
    result = []
    for i in s:
        if result:
            if result[-1] == '(' and i == ')':
                result.pop()
            else:
                result.append(i)
        else:
            result.append(i)
    return False if result else True
