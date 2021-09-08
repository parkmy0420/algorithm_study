n = 78
# n = 15
# n = 6

def solution(n):
    one_cnt = format(n, 'b').count('1') # n의 이진수에서 1 개수

    for i in range(n+1, 1000001):
        if one_cnt == format(i,'b').count('1'):
            return i

print(solution(n))