def solution(arrangement):
    arrangement = arrangement.replace('()', 'a')
    x = 0
    cut = 0
    for s in arrangement:
        if s == 'a':
            cut += x
        elif s == '(':
            x += 1
            cut += 1
        else:
            x -= 1
    return cut
