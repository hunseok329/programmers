def solution(msg):
    answer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = []
    while len(msg):
        num = 1
        while num < len(msg)+2:
            num += 1
            if msg[:num] not in answer:
                break
        answer.append(msg[:num])
        result.append(answer.index(msg[:num-1])+1)
        msg = msg[num-1:]
    return result
