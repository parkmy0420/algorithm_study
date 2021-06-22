n = 12345
def solution(n):
    answer = []
    n = list(reversed(str(n)))
    for i in range(len(n)):
        answer.append(int(n[i]))
    return answer

print(solution(n))