def dfs(x, check):
    global cnt
    check[x] = True     # x 노드 방문 표시
    for k in graph[x]:  # x 노드와 연결된 아직 방문하지 않은 노드를 재귀호출
        if not check[k]:
            cnt += 1
            dfs(k, check)

import sys
input = sys.stdin.readline
v = int(input())
e = int(input())
cnt = 0
graph = [[] for _ in range(v+1)]

for _ in range(e):  # 인접리스트 생성
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

check = [False]*(v+1)
dfs(1, check)
print(cnt)
