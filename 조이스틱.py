def solution(name):
    arr = [min((ord('Z') - ord(x) + 1), ord(x) - ord('A')) for x in name]
    
    result = 0
    myIndex = 0
    while True:
        if arr[myIndex] != 0:
            result += arr[myIndex]
            arr[myIndex] = 0
        if sum(arr) == 0:
            break
        check = True
        index = 1
        while True:
            if arr[myIndex + index] != 0 or arr[myIndex - index] != 0:
                    if arr[myIndex + index] != 0:
                        check = True
                    elif arr[myIndex - index] != 0:
                        check = False
                    break
            else:
                index += 1
        if check:
            result += index
            myIndex += index
        else:
            result += index
            myIndex -= index
    return result