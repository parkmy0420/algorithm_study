n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

def paper(matrix, n, s1, s2, cnt):
    start = matrix[s1][s2]
    if n != 1:
        for i in range(s1, s1+n):
            for j in range(s2, s2+n):
                if matrix[i][j] != start:
                    for k in range(0, n, n//3): # 9등분하기
                        for l in range(0, n, n//3):
                            cnt = paper(matrix, n//3, s1+k, s2+l, cnt)
                    return cnt

    if start == -1:
        cnt[0] += 1
    elif start == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1
    return cnt

cnt = paper(matrix, n, 0, 0, [0, 0, 0])
[print(cnt[i]) for i in range(3)]