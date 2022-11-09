def solution(a, b, n):
    answer = 0
    while n >= a:
        temp, r = divmod(n, a)
        answer += (temp*b)
        n = (temp*b) + r

    return answer


# print(solution(2, 1, 20))
print(solution(3, 2, 20))
# print(solution(5, 1, 20))