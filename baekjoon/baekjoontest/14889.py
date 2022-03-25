# 14889 스타트와 링크
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cp = int(1e9)   # 두 팀 능력치 차이 최소값 저장
teamnum = n//2
player = [i for i in range(0, n)]
team1_cb = list(combinations(player, teamnum))  # 조합

for i in team1_cb:
    temp_t1, temp_t2 = 0, 0     # 팀당 선수들 능력치 합계
    team1, team2 = list(i), list(set(player) - set(i))   # 선수 명단
    for j in range(teamnum):
        t1_p1, t2_p1 = team1[j], team2[j]   # t1, t2 첫번째 선수
        for k in range(j+1, teamnum):
            t1_p2, t2_p2 = team1[k], team2[k]   # t1, t2 두번째 선수
            temp_t1 += (graph[t1_p1][t1_p2] + graph[t1_p2][t1_p1])
            temp_t2 += (graph[t2_p1][t2_p2] + graph[t2_p2][t2_p1])
    cp = min(cp, abs(temp_t1 - temp_t2))
    if cp == 0: break
print(cp)
