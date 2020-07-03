def solution(number, k):
    length = len(number)
    idx = 0
    for _ in range(k):
        for i in range(idx, length):
            if(i == length - 1):
                number = number[:i]
            elif(number[i] < number[i+1]):
                number = (number[:i] + number[i+1:])
                idx = max(0, i - 1)
                break
        length -= 1
    return number
