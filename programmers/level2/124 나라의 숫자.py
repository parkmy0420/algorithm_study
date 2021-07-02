n = 1
# n = 2
# n = 3
# n = 9
# n = 24

def solution(n):
    answer = ''
    while n > 0:
        temp = list(divmod(n, 3))
        if temp[1] == 0:
            answer = '4' + answer
            n = temp[0] - 1
        else:
            answer = ''.join(str(temp[1])) + answer
            n = temp[0]
    return answer

print(solution(n))