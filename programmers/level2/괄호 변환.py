# p = "(()())()"
p = ")("
# p = "()))((()"

# 균형잡힌 괄호 문자열
def balance(p):
    num = 0
    for i in range(len(p)):
        if p[i] == '(':
            num -= 1
        else:
            num += 1
        if num == 0:
            # u, v 분리
            u, v = p[:i+1], p[i+1:]
            break
    return u, v

# 올바른 괄호 문자열
def isright(pstr):
    temp = []
    for i in pstr:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    if len(temp) != 0:
        return False
    return True

# 뒤집기
def reverse(u):
    return [')' if i == '(' else '(' for i in u]

# 재귀함수
def recursive(u):
    if len(u) == 0:
        return ''
    u, v = balance(u)
    if isright(u):
        return u + recursive(v)
    else:
        return '(' + recursive(v) + ')' + ''.join(reverse(u[1:-1]))

def solution(p):
    if len(p) == 0 or isright(p):
        return p
    else:
        return recursive(p)






print(solution(p))