# s = "()()"
s = "(())()"
# s = ")()("
# s = "(()("

def solution(s):
    temp = []
    for i in s:
        if i == '(':
            temp.append(i)
        else:
            if not temp:
                return False
            if temp[-1] == '(':
                temp.pop()
    return True if not temp else False

print(solution(s))


