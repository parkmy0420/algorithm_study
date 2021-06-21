# n = 3
n = 4

def solution(n):
    sbstr = '수박'
    answer = ''
    for i in range(n):
        answer += sbstr[i % 2]
    return answer

print(solution(n))