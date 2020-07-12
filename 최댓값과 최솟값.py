def solution(s):
    number = [int(x) for x in s.split()]
    return str(min(number)) + ' ' + str(max(number))
