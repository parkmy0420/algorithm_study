from collections import deque
def solution(n, computers):
    answer, visited = 0, [0]*n
    def bfs(i):
        q = deque([i])
        visited[i] = 1
        while q:
            now = q.popleft()
            for j in range(n):
                if computers[now][j] == 1 and visited[j] == 0 and now != j:
                    visited[j] = 1
                    q.append(j)

    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))