def solution(s):
    answer = ''
    if len(s) < 2:
        return len(s)
    for i in range(1, (len(s)//2)+1):
        result = ''
        check = []
        count = []
        num = 0
        for j in range(i, len(s)+1, i):
            if len(check) == 0:
                check.append(s[num:j])
                count.append(1)
                num = j
            elif check[-1] != s[num:j]:
                check.append(s[num:j])
                count.append(1)
                num = j
            elif check[-1] == s[num:j]:
                count[-1] += 1
                num = j
        if num != len(s):
            check.append(s[num:])
            count.append(1)
        for w in range(len(check)):
            if count[w] != 1:
                result += (str(count[w]) + check[w])
            else:
                result += check[w]
        if len(answer) == 0:
            answer = result
        elif len(answer) > len(result):
            answer = result
    return len(answer)
