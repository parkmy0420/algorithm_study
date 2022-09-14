# 4949 균형잡힌 세상
import sys
input = sys.stdin.readline
while True:
    stack = []
    a = input()
    print(a)
    if a == '.\n':
        break
    else:
        acheck, a = 0, list(a)
        for i in a:
            acheck += 1
            if i in ['(', '[']:     # 열린 괄호
                stack.append(i)
            elif i in [')', ']']:  # 닫힌 괄호
                if not stack:  # 빈 stack인 경우
                    stack.append(i)
                    break
                if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    stack.append(i)
                    break
        if acheck == len(a):
            if not stack:
                print('yes')
            else:
                print('no')
        else:
            print('no')