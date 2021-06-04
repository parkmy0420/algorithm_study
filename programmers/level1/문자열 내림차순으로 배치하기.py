s = 'ZAbcdefg'

def solution(s):
    return "".join(sorted(s,reverse=True))

print(solution(s))

#처음 문제를 잘못보고 오름차순으로 잘 못 정렬해서 대문자가 앞에 나오는 경우 만든 것
# def solution(s):
#     answer = sorted(s,reverse=True)
#     for i in range(len(answer)):
#         if ord(answer[0]) < 97:
#             answer.append(answer.pop(0))
#         else:
#             break
#     return "".join(answer)