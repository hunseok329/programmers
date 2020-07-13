def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2[0])
    c = len(arr2)
    result = [[0 for _ in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result
