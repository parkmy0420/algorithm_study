# s = 'baabaa'
# s = 'cdcd'
# s = 'aabkee'
s = 'aabbbbee'


def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0: return 1
    else: return 0

print(solution(s))