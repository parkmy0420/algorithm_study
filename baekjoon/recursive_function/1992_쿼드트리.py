def rf(s1, s2, e1, e2):
    start = graph[s1][s2]
    tf = True
    for i in range(s1, e1):
        for j in range(s2, e2):
            if graph[i][j] != start:
                tf = False
                print('(', end='')
                rf(s1, s2, (s1+e1)//2, (s2+e2)//2)
                rf(s1, (s2+e2)//2, (s1+e1)//2, e2)
                rf((s1+e1)//2, s2, e1, (s2+e2)//2)
                rf((s1+e1)//2, (s2+e2)//2, e1, e2)
                print(')', end='')
                break
        if not tf:
            break
    if tf:
        print(start, end='')

import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
rf(0, 0, n, n)
