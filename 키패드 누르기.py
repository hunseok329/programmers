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




def distance(current_loc, target_loc):
    x = abs(current_loc[0] - target_loc[0])
    y = abs(current_loc[1] - target_loc[1])
    return x + y

def solution(numbers, hand):
    answer = ''
    
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2),
               '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    
    left = "*"
    right = "#"
    
    for num in numbers:
        if num in [1, 4, 7]:
            left = num
            answer += "L"
        elif num in [3, 6, 9]:
            right = num
            answer += "R"
        else:
            left_distance = distance(key_dict[left], key_dict[num])
            right_distance = distance(key_dict[right], key_dict[num])
            if left_distance == right_distance:
                if hand == "left":
                    left = num
                    answer += "L"
                else:
                    right = num
                    answer += "R"
            elif left_distance < right_distance:
                left = num
                answer += "L"
            else:
                right = num
                answer += "R"
    return answer