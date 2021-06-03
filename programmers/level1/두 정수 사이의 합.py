a = 5
b = 3

def solution(a, b):
    answer = 0
    if a <= b :
        for i in range(0,b-a+1):
            answer += (a + i)
    else :
        for i in range(0,a-b+1):
            answer += (b + i)

    return answer

print(solution(a,b))