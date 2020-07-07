def solution(prices):
    result = []
    for i in range(len(prices)):
        check = True
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                result.append(j-i)
                check = False
                break
        if check == True:
            result.append((len(prices)-1)-i)
    return result
