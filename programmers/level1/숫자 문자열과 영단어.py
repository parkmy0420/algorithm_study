# s = "one4seveneight"
s = "23four5six7"
# s = "2three45sixseven"
# s = "123"
def solution(s):
    num = {'zero': '0','one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10'}
    answer, temp = [],[]

    if s.isdigit():
        return int(s)
    else:
        for i in s:
            if i.isdigit():
                answer.append(i)
            else:
                temp.append(i)
            if ''.join(temp) in num:
                answer.append(num[''.join(temp)])
                temp = []

    return int(''.join(answer))

print(solution(s))