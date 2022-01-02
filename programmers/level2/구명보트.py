from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people))

    while len(q) != 0:
        if len(q) != 1 and q[0]+q[-1] <= limit:
            q.popleft()
        answer += 1
        q.pop()

    return answer

print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))