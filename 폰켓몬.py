def solution(nums):
    half = len(nums)//2
    length = len(set(nums))
    return length if half >= length else half
