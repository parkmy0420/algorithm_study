# priorities, location = [2, 1, 3, 2], 2
# priorities, location = [1, 1, 9, 1, 1, 1], 0
# priorities, location = [1, 3, 2, 1, 1], 2
priorities, location = [1, 5, 9, 3, 2, 2, 1, 7], 5

def solution(priorities, location):
    from collections import deque
    deq = deque(priorities)
    i = 0
    a = max(deq)
    temp = []

    while True:
        if deq[i] == a:
            if i == location:
                return len(temp) + 1
            else:
                location -= 1
            temp.append(deq.popleft())
        else:
            if i == location:
                location = len(deq)-1
            else:
                location -= 1
            deq.append(deq.popleft())

        a = max(deq)



print(solution(priorities, location))