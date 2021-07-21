n = 5

#재귀함수를 통한 팩토리얼 구현
def factorial_recursion(n):
    if n > 1:
        return n * factorial_recursion(n-1)
    else:
        return 1

# for문을 통한 팩토리얼 구현
def factorial_for(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

# math 라이브러리
import math

def solution(n):
    return f'재귀 = {factorial_recursion(n)}, facfor = {factorial_for(n)}, facmath = {math.factorial(n)}'

print(solution(n))