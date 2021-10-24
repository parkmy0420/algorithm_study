n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]

def colorpaper(paper, s1, e1, s2, e2, cnt):
    start = paper[s1][e1]
    for i in range(s1, s2):
        for j in range(e1, e2):
            if paper[i][j] != start:    # 정사각형 색상이 모두 같지 않으면 4분할
                cnt = colorpaper(paper, s1, e1, (s1+s2)//2, (e1+e2)//2, cnt)
                cnt = colorpaper(paper, s1, (e1+e2)//2, (s1+s2)//2, e2, cnt)
                cnt = colorpaper(paper, (s1+s2)//2, e1, s2, (e1+e2)//2, cnt)
                cnt = colorpaper(paper, (s1+s2)//2, (e1+e2)//2, s2, e2, cnt)
                return cnt
    if start == 1:  # 파란색 색종이
        cnt[1] += 1
    else:   # 하얀색 색종이
        cnt[0] += 1
    return cnt

cnt = colorpaper(paper, 0, 0, n, n, [0, 0])
print(cnt[0])
print(cnt[1])