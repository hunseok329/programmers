def solution(heights):
    length = len(heights)
    result = [0]*length
    reverse = heights[::-1]
    for i in range(length):
        for j in range(i+1, length):
            if reverse[i] < reverse[j]:
                result[i] = length-j
                break
    return result[::-1]
