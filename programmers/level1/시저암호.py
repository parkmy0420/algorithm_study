# s = "AB"
# n = 1
# s = "z"
# n = 1
s = "a B z"
n = 4

def solution(s, n):
    answer =''
    for i in s:
        if i ==' ':
            answer += ' '
        elif i >= 'a' and i <= 'z':
            if chr(ord(i) + n) > 'z':
                answer += (chr(ord(i) + n - 26))
            else: answer += (chr(ord(i) + n))
        else:
            if chr(ord(i) + n) > 'Z':
                answer += (chr(ord(i) + n - 26))
            else: answer += (chr(ord(i) + n))

    return answer

print(solution(s,n))