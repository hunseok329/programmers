def solution(bridge_length, weight, truck_weights):
    bridge = []
    count = 0
    bridge_weight = 0
    while truck_weights:
        count += 1
        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        if len(bridge) == bridge_length:
            bridge_weight -= bridge[0]
            del bridge[0]
    return count + bridge_length


from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    cnt = 0
    bridge_weigths = 0
    truck_weights.reverse()

    while truck_weights:
        cnt += 1
        if bridge_weigths + truck_weights[-1] <= weight:
            bridge_weigths += truck_weights[-1]
            bridge.append(truck_weights.pop())
        else:
            bridge.append(0)
        if len(bridge) == bridge_length:
            bridge_weigths -= bridge.popleft()
    return cnt + bridge_length



from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    cnt = 0
    bridge_weigths = 0
    truck_weights.reverse()

    while truck_weights:
        bridge_weigths -= bridge.popleft()
        cnt += 1
        
        if bridge_weigths + truck_weights[-1] <= weight:
            bridge_weigths += truck_weights[-1]
            bridge.append(truck_weights.pop())
        else:
            bridge.append(0)
            
    return cnt + bridge_length