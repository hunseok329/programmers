def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        hint = [str(bin(arr1[i])[2:]), str(bin(arr2[i])[2:])]
        for index, hi in enumerate(hint):
            if len(hi) != n:
                hint[index] = "0"*(n-len(hi)) + hi
        answer = ''
        for j in range(n):
            if hint[0][j] == '1' or hint[1][j] == '1':
                answer += "#"
            else:
                answer += " "
        result.append(answer)
    return result
