# x, n = 2, 5
# # x, n = 4, 3
x, n = -4, 2

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

print(solution(x, n))