def bfs(x, check):
    queue = deque([x])
    check[x] = True     # x 노드 방문 표시
    while queue:    # 큐가 빌 때까지
        k = queue.popleft()
        for y in graph[k]:
            if not check[y]:    # x 노드와 연결된 방문하지 않은 원소들을 큐에 삽입
                queue.append(y)
                check[y] = True

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [True]+[False]*n
cnt = 0

for _ in range(m):  # 인접리스트 생성
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

while False in visited:     # 방문하지 않은 노드가 없을때까지 반복
    cnt += 1
    bfs(visited.index(False), visited)
print(cnt)