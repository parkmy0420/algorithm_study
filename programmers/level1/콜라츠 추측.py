# num = 6
num = 16
# num = 626331

def solution(num):
    cnt = 0
    while num != 1 :
        if num % 2 == 0:
            num = num /2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
    return -1 if cnt > 499 else cnt

print(solution(num))