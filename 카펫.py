def solution(brown, yellow):
    result = []
    add = brown + yellow
    for i in range(1, yellow+1):
        if yellow % i == 0:
            result.append(i)
    for num in range(len(result)//2+1):
        if (result[num]+2) * (result[-(num+1)]+2) == add:
            return [result[-(num+1)]+2, result[num]+2]
