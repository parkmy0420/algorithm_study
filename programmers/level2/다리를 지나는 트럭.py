# bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
# bridge_length, weight, truck_weights = 100, 100, [10]
bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]


def solution(bridge_length, weight, truck_weights):
    onweight, answer, queue, time = 0, 0, [], []

    while True:
        if len(truck_weights) != 0:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
                time.append(0)
        elif not queue:
            return answer + 1

        for i in range(len(time)):
            time[i] = time[i] + 1
        answer += 1

        if time[0] == bridge_length:
            queue.pop(0)
            time.pop(0)


print(solution(bridge_length,weight,truck_weights))
