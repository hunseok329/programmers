def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    thrid = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            count[0] += 1
        if answers[i] == second[i % 8]:
            count[1] += 1
        if answers[i] == thrid[i % 10]:
            count[2] += 1
    return [index + 1 for index, value in enumerate(count) if value == max(count)]
