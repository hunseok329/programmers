def solution(clothes):
    string = {}
    count = 0
    for _, kind in clothes:
        if kind in string:
            string[kind] += 1
        else:
            string[kind] = 2
    for num in string.values():
        if count != 0:
            count *= num
        else:
            count += num
    return count - 1
