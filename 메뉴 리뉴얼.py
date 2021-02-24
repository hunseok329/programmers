from itertools import combinations
from collections import Counter
def solution(orders, course):
    
    
    result = []

    for c in course:
        check = []
        for x in orders:
            combi = combinations(sorted(x), c)
            check += combi
        counter = Counter(check)
        if len(counter) != 0 and max(counter.values()) != 1:
            for z in counter:
                if counter[z] == max(counter.values()):
                    result.append(''.join(z))
    return sorted(result)