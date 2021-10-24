n, n1, n2 = map(int, input().split())
cnt = 0
def divide(n, n1, n2, cnt):
    if n > 1:   # n이 1보다 크면 4분할
        # time - 찾는 사분면 위치 - 1(방문한 횟수를 곱하기 위함), temp = 사분면 한 변 길이
        time, temp = 0, int((2 ** n) / 2)
        if n1 >= temp:  # n1이 3, 4분면 중에 있는 경우
            time += 2
            n1 -= temp  # 찾는 행과 열이 있는 사분면의 첫번째 원소를 0, 0 으로 만들기 위해
        if n2 >= temp: # n1이 2, 4분면 중에 있는 경우
            time += 1
            n2 -= temp  # 찾는 행과 열이 있는 사분면의 첫번째 원소를 0, 0 으로 만들기 위해
        cnt += temp * temp * time   # 찾는 행과 열이 있는 사분면 앞에 있는 사분면들의 방문 횟수
        cnt = divide(n-1, n1, n2, cnt)
    else:   # 4분할 하지 못하는 마지막 사분면에서의 방문 횟수
        cnt += (n1*2 + n2 + 1)
    return cnt

print(divide(n, n1, n2, cnt)-1)