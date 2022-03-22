# 14500 테르로미노
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shapes = [
    [(0,0),(0,1),(0,2),(0,3)],  # ㅡ
    [(0,0),(1,0),(2,0),(3,0)],  # ㅣ
    [(0,0),(0,1),(1,0),(1,1)],  # ㅁ
    [(0,0),(1,0),(1,1),(2,1)],  # 4가지 계단모양
    [(0,1),(1,0),(1,1),(2,0)],
    [(1,0),(0,1),(1,1),(0,2)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)],  # ㅜ
    [(0,1),(1,0),(1,1),(1,2)],  # ㅗ
    [(0,0),(1,0),(2,0),(1,1)],  # ㅏ
    [(1,0),(0,1),(1,1),(2,1)],  # ㅓ
    [(0,0),(1,0),(1,1),(1,2)],  # 8가지 ㄴ 모양
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(2,0),(0,1),(1,1),(2,1)]
]

answer = 0
for i in range(n):
    for j in range(m):
        for shape in shapes:
            temp = 0
            for k in range(4):
                try: temp += graph[i+shape[k][0]][j+shape[k][1]]
                except IndexError: break
            answer = max(temp, answer)
print(answer)









