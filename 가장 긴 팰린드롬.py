def solution(s):
    result = 0
    if len(s) < 2:
        return 1
    for i in range(1, len(s)+1):
        j = 0
        while i+j <= len(s):
            p = s[j:j+i]
            if p == p[::-1]:
                result = i
            j += 1
    return result
