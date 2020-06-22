def solution(d, budget):
    d.sort()
    count = 0
    for num in d:
        if budget - num >= 0:
            count += 1
            budget -= num
        else:
            return count
    return count
