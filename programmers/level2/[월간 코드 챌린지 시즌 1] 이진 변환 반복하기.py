# s = '110010101001'
s = '01110'
# s = '1111111'

def solution(s):
    temp, answer = s, [0,0]
    while temp != '1':
        temp = s.replace('0','')
        answer[1] += len(s) - len(temp)
        temp = format(len(temp), 'b')
        s = temp
        answer[0] += 1
    return answer

print(solution(s))