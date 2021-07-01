# x = 10
# x = 12
x = 11
# x = 13

def solution(x):
    return True if x % sum(list(map(int, str(x)))) == 0 else False

print(solution(x))