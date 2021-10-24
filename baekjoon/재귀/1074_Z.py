n, n1, n2 = map(int, input().split())
cnt = 0
def divide(n, n1, n2, cnt):
    if n > 1:
        time, temp = 0, int((2 ** n) / 2)
        if n1 >= temp:
            time += 2
            n1 -= temp
        if n2 >= temp:
            time += 1
            n2 -= temp
        cnt += temp * temp * time
        cnt = divide(n-1, n1, n2, cnt)
    else:
        cnt += (n1*2 + n2 + 1)
    return cnt

print(divide(n, n1, n2, cnt)-1)

