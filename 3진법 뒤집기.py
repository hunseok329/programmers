def solution(n):
    arr = []
    result = 0
    while 0 < n:
        n, mod = divmod(n, 3)
        arr.append(mod)
        
    num = 1
    
    for i in range(len(arr)-1, -1, -1):
        result += arr[i] * num
        num *= 3
    return result