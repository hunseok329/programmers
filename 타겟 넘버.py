from itertools import combinations


def solution(numbers, target):
    sumNumber = sum(numbers)
    length = len(numbers)
    count = 0
    for j in numbers:
        if sumNumber - (j*2) == target:
            count += 1
    for i in range(2, length):
        p = list(combinations(numbers, i))
        for num in p:
            if sumNumber - (sum(num)*2) == target:
                count += 1
    return count
