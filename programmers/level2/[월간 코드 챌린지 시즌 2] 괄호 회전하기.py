s = "[](){}"
# s = "}]()[{"
# s = "[)(]"
# s = "}}}"

from collections import deque
def check(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i in ['[', '(', '{']:
            stack.append(i)
        elif (i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{'):
            del stack[-1]
        else:
            stack.append(i)

    return len(stack) == 0


def solution(s):
    answer = 0
    deq = deque(s)

    for i in range(len(s)):
        if check(deq) == True:
            answer += 1
        deq.rotate(-1)

    return answer


print(solution(s))