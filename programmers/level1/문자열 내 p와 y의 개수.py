# s = "pPoooyY"
# s = "Pyy"
s = 'ans'

def solution(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution(s))