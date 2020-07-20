def solution(str1, str2):
    fir = []
    sec = []
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            fir.append((str1[i]+str1[i+1]).upper())
    for j in range(len(str2)-1):
        if (str2[j]+str2[j+1]).isalpha():
            sec.append((str2[j]+str2[j+1]).upper())

    gyo = set(fir) & set(sec)
    hap = set(fir) | set(sec)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(fir.count(gg), sec.count(gg))for gg in gyo])
    hap_sum = sum([max(fir.count(hh), sec.count(hh))for hh in hap])

    return int((gyo_sum/hap_sum)*65536)
