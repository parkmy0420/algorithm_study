cnt = int(input())

def hanoi(cnt, start, end):
    if cnt > 1:
        hanoi(cnt-1, start, 6-start-end)
    print(start, end)
    if cnt > 1:
        hanoi(cnt-1, 6-start-end, end)

print(2**cnt - 1)
hanoi(cnt, 1, 3)