# brown, yellow = 10, 2
# brown, yellow = 8, 1
brown, yellow = 24, 24


def roots(b, c): # 근의 공식 구하기 x^2 -bx + c
    D = (b*b-4*c)**0.5
    x1 = (-b+D)/2
    x2 = (-b-D)/2
    return int(x1), int(x2)

def solution(brown, yellow):
    plus = -int((brown + 4)/2)
    x1, x2 = roots(plus, brown+yellow)
    return [max(x1, x2), min(x1, x2)]



## 위의 코드 더 짧게 구현해 보기
# def roots(b, c): # 근의 공식 구하기 x^2 -bx + c
#     return int((-b+((b*b-4*c)**0.5))/2), int((-b-((b*b-4*c)**0.5))/2)
#
# def solution(brown, yellow):
#     x1, x2 = roots(-int((brown + 4)/2), brown+yellow)
#     return [max(x1, x2), min(x1, x2)]


print(solution(brown, yellow))
