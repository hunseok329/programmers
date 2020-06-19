def solution(s, n):
    result = ''
    for i in s:
        if i == ' ':
            result += i
            continue
        if (ord(i) < 91 and 90 < ord(i) + n) or (96 < ord(i) < 123 and 122 < ord(i) + n):
            result += chr(ord(i) + n - 26)
            continue
        result += chr(ord(i)+n)
    return result
