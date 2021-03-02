from itertools import permutations

def cal(left, right, ca):
    if ca == '*':
        return left * right
    elif ca == '-':
        return left - right
    else:
        return left + right

def solution(expression):
    check = list(permutations('*-+', 3))
    
    answer = 0
    
    for x in check:
        x = list(x)

        temp = []
        j = 0
        for i in range(len(expression)):
            if expression[i] == '*' or expression[i] == '-' or expression[i] == '+':
                temp.append(expression[j:i])
                temp.append(expression[i])
                j = i+1
        temp.append(expression[j:len(expression)])

        while x:
            if x[-1] not in temp:
                x.pop()
                continue
            else:
                i = temp.index(x[-1])
                temp[i-1] = cal(int(temp[i-1]), int(temp[i+1]), x[-1])
                temp.pop(i)
                temp.pop(i)
        if abs(temp[0]) > answer:
            answer = abs(temp[0])
    return answer