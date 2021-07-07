# progresses, speeds = [93, 30, 55], [1, 30, 5]
progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    import math
    answer, stack = [], []

    for i in range(len(progresses)):
        temp = math.ceil((100 - progresses[i]) / speeds[i])
        if not stack: # stack 비었는지 확인
            stack.append(temp)
        elif max(stack) < temp:
            answer.append(len(stack))
            stack.clear()
            stack.append(temp)
        else:
            stack.append(temp)
    answer.append(len(stack))

    return answer

print(solution(progresses,speeds))