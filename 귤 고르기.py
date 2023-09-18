from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    cnt_list = sorted(Counter(tangerine).values(), reverse=True)
    
    for cnt in cnt_list:
        if k <= 0:
            return answer
        k -= cnt
        answer += 1
    return answer