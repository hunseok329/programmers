def distance(r1, r2):
    x = abs(r1[0] - r2[0])
    y = abs(r1[1] - r2[1])
    return x + y

def solution(numbers, hand):
    keypad = {1 : [0,3], 2 : [1, 3], 3 : [2, 3], 4 : [0, 2], 5 : [1, 2], 6 : [2, 2], 7 : [0, 1], 8 : [1, 1], 9 : [2, 1], 0 : [1, 0]}
    
    left_hand = [0, 0]
    right_hand = [2, 0]
    result = ''
    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left_hand = keypad[num]
        elif num in [3, 6, 9]:
            result += 'R'
            right_hand = keypad[num]
        else:
            left = distance(left_hand, keypad[num])
            right = distance(right_hand, keypad[num])
            print(left, right)
            if left < right:
                result += 'L'
                left_hand = keypad[num]
            elif left > right:
                result += 'R'
                right_hand = keypad[num]
            else:
                if hand == "right":
                    result += 'R'
                    right_hand = keypad[num]
                else:
                    result += 'L'
                    left_hand = keypad[num]
    return result