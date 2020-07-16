from itertools import permutations


def solution(numbers):
    sumP = []
    count = 0
    for s in range(1, len(numbers)+1):
        p = list(permutations(numbers, s))
        for num in set(p):
            sumP.append(int(''.join(num)))
    sumP = set(sumP)
    for w in sumP:
        if w == 1 or w == 0:
            continue
        for n in range(2, w//2+1):
            if w % n == 0:
                break
        else:
            count += 1
    return count
