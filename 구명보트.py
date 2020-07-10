def solution(people, limit):
    people = sorted(people, reverse=True)
    length = len(people)
    count = 0
    num = 0
    while num < length:
        if people[num] + people[-1] <= limit:
            people.pop()
            length -= 1
        count += 1
        num += 1
    return count
