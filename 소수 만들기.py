# from itertools import combinations

# def solution(nums):
#     p = list(combinations(nums, 3))
#     s = [list(x) for x in p]
#     notCount = 0
#     for num in s:
#         if sum(num) == 0 or sum(num) == 1:
#             notCount += 1
#             break
#         for i in range(2, sum(num)//2):
#             if sum(num) % i == 0:
#                 notCount += 1
#                 break
#     return len(p) - notCount

from itertools import combinations


def solution(nums):
    result = 0
    for num in combinations(nums, 3):
        number = sum(num)
        for i in range(2, number//2):
            if number % i == 0:
                break
        else:
            result += 1
    return result
