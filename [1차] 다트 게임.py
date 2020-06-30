import re


def solution(dartResult):
    result = []
    square = {'S': 1, 'D': 2, 'T': 3}
    scores = re.split('\D', dartResult)
    squares = re.split('\d', dartResult)
    scores = list(filter(lambda x: x != '', scores))
    squares = list(filter(lambda x: x != '', squares))
    for num in range(len(scores)):
        if len(squares[num]) == 1:
            result.append(int(scores[num])**square[squares[num]])
        else:
            if squares[num][-1] == '*':
                if len(result) != 0:
                    result[-1] = result[-1] * 2
                result.append(int(scores[num])**square[squares[num][0]]*2)
            else:
                result.append(int(scores[num])**square[squares[num][0]]*(-1))
    return sum(result)
