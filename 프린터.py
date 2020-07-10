def solution(priorities, location):
    printer = [[i, v] for i, v in enumerate(priorities)]
    priorities = sorted(priorities)
    result = []
    num = 0
    while len(priorities) != 0:
        if num >= len(printer):
            num = 0
        if priorities[-1] != printer[num][-1]:
            num += 1
        else:
            priorities.pop()
            result.append(printer[num])
            num += 1
    for x in range(len(result)):
        if result[x][0] == location:
            return x + 1
