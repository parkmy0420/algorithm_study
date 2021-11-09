def dfs(x, check):
    check[x] = True     # x 노드 방문 표시
    print(x, end=' ')
    for k in glist[x]:  # x 노드와 연결된 아직 방문하지 않은 노드를 재귀호출
        if not check[k]:
            dfs(k, check)

def bfs(x, check):
    queue = deque([x])
    check[x] = True     # x 노드 방문 표시
    while queue:    # 큐가 빌 때까지
        k = queue.popleft()
        print(k, end=' ')
        for y in glist[k]:
            if not check[y]:    # x 노드와 연결된 방문하지 않은 원소들을 큐에 삽입
                queue.append(y)
                check[y] = True

import sys
from collections import deque
input = sys.stdin.readline
v, e, n = map(int, input().split())
glist = [[] for _ in range(v+1)]
vsort = []

for _ in range(e):  # 인접리스트 생성
    i, j = map(int, input().split())
    glist[i].append(j)
    glist[j].append(i)
    vsort.append(i)
    vsort.append(j)

set(vsort)
for i in vsort:     # 간선이 있는 노드만 정렬
    glist[i].sort()

check = [False]*(v+1)
dfs(n, check)
print()
check = [False]*(v+1)
bfs(n, check)