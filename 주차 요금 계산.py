from math import ceil
from collections import defaultdict

def convert_time(time):
    h, m = map(int, time.split(":"))
    return (h * 60) + m

def billing(time, default_time, default_pay, fee_time, fee_pay):
    if time <= default_time:
        return default_pay
    else:
        over_time = time - default_time
        over_pay = (ceil(over_time / fee_time) * fee_pay)
        return default_pay + over_pay

def solution(fees, records):
    default_time, default_pay, fee_time, fee_pay = fees
    parking = {}
    answer = defaultdict(int)

    for record in records:
        time, car_num, action = record.split()
        time = convert_time(time)
        
        if action == "IN":
            parking[car_num] = time
        else:
            answer[car_num] += (time - parking[car_num])
            del parking[car_num]

    if parking:
        for car in parking:
            answer[car] += (1439 - parking[car])

    for car in answer:
        answer[car] = billing(answer[car], default_time, default_pay, fee_time, fee_pay)

    return [answer[key] for key in sorted(answer)]