# s = "aabbaccca"
s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = 'a'

def solution(s):
    stack, temp, cnt = [], [], []
    if len(s) == 1:
        return 1
    else:
        for i in range(1, int((len(s))/2)+1):
            slist = list(s)
            for j in range(0, len(s), i):
                if not stack: #스택이 비었을 때
                    stack.append(''.join(slist[:i]))
                    del slist[:i]
                    continue
                elif len(slist) < i: # 자르는 문자열 갯수보다 남은 문자열 갯수가 작을 때
                    temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
                    stack.clear()
                    temp.append(''.join(slist[:i]))
                    del slist[:i]
                else:
                    if stack[-1] != ''.join(slist[:i]):
                        temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
                        stack.clear()

                    stack.append(''.join(slist[:i]))
                    del slist[:i]

                    if j == len(s) - i: # 마지막 인덱스 일때
                        temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
                        stack.clear()

            cnt.append(len(''.join(temp)))
            temp, stack = [], []
        return min(cnt)

# def solution(s):
#     stack, temp, cnt = [], [], []
#
#     for i in range(1, len(s)):
#         slist = list(s)
#         for j in range(0, len(s), i):
#             if not stack: #스택이 비었을 때
#                 stack.append(''.join(slist[:i]))
#                 del slist[:i]
#                 continue
#             elif len(slist) < i: # 자르는 문자열 갯수보다 남은 문자열 갯수가 작을 때
#                 temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
#                 stack.clear()
#                 temp.append(''.join(slist[:i]))
#                 del slist[:i]
#             else:
#                 if stack[-1] == ''.join(slist[:i]):
#                     if j != len(s) - i: # 마지막 인덱스 일때
#                         stack.append(''.join(slist[:i]))
#                         del slist[:i]
#                     else:
#                         stack.append(''.join(slist[:i]))
#                         del slist[:i]
#                         temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
#                         stack.clear()
#                 else:
#                     if j != len(s) - i:
#                         temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
#                         stack.clear()
#                         stack.append(''.join(slist[:i]))
#                         del slist[:i]
#                     else:
#                         temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
#                         stack.clear()
#                         stack.append(''.join(slist[:i]))
#                         del slist[:i]
#                         temp.append(str(len(stack)) + str(''.join(stack[-1])) if len(stack) != 1 else str(''.join(stack[-1])))
#                         stack.clear()
#
#         cnt.append(len(''.join(temp)))
#         temp, stack = [], []
#
#     return min(cnt)

print(solution(s))