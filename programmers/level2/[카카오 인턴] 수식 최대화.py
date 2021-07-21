# expression = "100-200*300-500+20"
expression = "50*6-3*2"
# expression = "100-200+20"


def calculation(pmt_operator, listexpression):
    tf, j, num = True, 0, listexpression.copy()
    for i in range(len(pmt_operator)):
        while tf:
            if num[j] == pmt_operator[i]:
                num[j-1] = str(eval(''.join(num[j-1:j+2])))
                del num[j:j+2]
            else: j += 1
            if pmt_operator[i] not in num:
                tf = False
        tf, j = True, 0
    return num


def solution(expression):
    from itertools import permutations
    temp, operator, listexpression = '', [], []
    answer = []

    # 숫자, 연산자 분리
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            listexpression.append(temp)
            temp = ''
            operator.append(i)
            listexpression.append(i)
    listexpression.append(temp)

    # 연산자 우선순위
    pmt_operator = list(permutations(set(operator)))

    for j in range(0, len(pmt_operator)):
        answer.append(abs(int(''.join(calculation(pmt_operator[j], listexpression)))))

    return max(answer)

print(solution(expression))


