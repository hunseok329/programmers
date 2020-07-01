def solution(x):
    x.sort()
    for num_1 in range(len(x)):
        for num_2 in range(num_1+1, len(x)):
            if x[num_1] == x[num_2][:len(x[num_1])]:
                return False
    return True
