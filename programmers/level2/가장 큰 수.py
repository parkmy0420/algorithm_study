# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
numbers = [3, 30, 34, 5, 9, 90]


def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda i: i*3, reverse=True)

    return str(int(''.join(numbers)))

print(solution(numbers))