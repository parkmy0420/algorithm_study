n = 118372
def solution(n):
    a = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(list(map(str, a))))

    # return int(''.join(sorted(list(str(n)),reverse = True)))

print(solution(n))