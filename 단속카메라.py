def solution(routes):
    routes = sorted(routes, key=lambda x : x[1])
    camera = -30001
    result = 0
    
    for route in routes:
        if camera < route[0]:
            result += 1
            camera = route[1]
    return result
