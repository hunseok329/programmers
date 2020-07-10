def solution(s):
    s = s.lower()
    word = [x for x in s]
    check = True
    for num in range(len(word)):
        if word[num] == ' ':
            check = True
        elif check == True:
            if word[num].isalpha():
                word[num] = word[num].upper()
                check = False
            else:
                check = False
    return ''.join(word)
