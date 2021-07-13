# n,a,b = 8, 4, 7
n,a,b = 16, 7, 13

def solution(n,a,b):
    cnt, tf = 1, True
    round = []
    while tf:
        for i in range(1, int(n/2)+1):
            round += [i, i]
        if round[a-1] == round[b-1]:
            tf = False
        else:
            n, a, b = n/2, round[a-1], round[b-1]
            cnt += 1
    return cnt

# 더 효율성 좋은 코드
# def solution(n,a,b):
#     cnt = 0
#     while a != b:
#         cnt += 1
#         a, b = (a+1)//2, (b+1)//2
#
#     return answer

print(solution(n,a,b))