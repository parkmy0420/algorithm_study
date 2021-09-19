# s = "1 2 3 4"
# s = "-1 -2 -3 -4"
s = "-1 -1"

def solution(s):
    s = list(map(int, s.split(' ')))
    return f'{min(s)} {max(s)}'


print(solution(s))