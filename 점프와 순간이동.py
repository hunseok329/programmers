def solution(n):
    count = 0
    while n > 0:
        div = n//2
        mod = n%2
        
        n = div
        if mod == 1:
            count += 1
    return count