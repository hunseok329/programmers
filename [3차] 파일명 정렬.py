import re
def solution(files):
    s = []
    for word in files:
        s.append(re.split(r'([0-9]+)', word))
    p = sorted(s, key=lambda x : (x[0].lower(), int(x[1])))
    return ["".join(x)for x in p]