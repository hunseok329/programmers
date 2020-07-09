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
