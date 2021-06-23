# n = 121
n =3

def solution(n):
    return (int(n**0.5)+1)**2 if int(n**0.5) == n**0.5 else -1

print(solution(n))