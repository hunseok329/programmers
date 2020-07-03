def solution(skill, skill_trees):
    result = []
    for tree in skill_trees:
        number = list(skill)
        check = True
        for ski in tree:
            if len(number) != 0:
                if ski in number and ski == number[0]:
                    del number[0]
                elif ski in number and ski != number[0]:
                    check = False
                    break
        result.append(check)
    return result.count(True)
