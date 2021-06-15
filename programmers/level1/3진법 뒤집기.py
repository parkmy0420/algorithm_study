# n = 45
n = 125

def solution(n):
    m = []
    while n >= 1:
        m.append(str(n % 3))
        n = n // 3
    return int(''.join(m), 3)

print(solution(n))