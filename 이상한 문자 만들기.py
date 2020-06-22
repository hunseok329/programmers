def solution(s):
    answer = ''
    upper = True
    for i in s:
        if i == " ":
            upper = True
            answer += " "
            continue
        if upper == True:
            answer += i.upper()
            upper = False
        else:
            answer += i.lower()
            upper = True
    return answer
