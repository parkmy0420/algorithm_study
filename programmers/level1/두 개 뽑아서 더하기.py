numbers = [2, 1, 3, 4, 1]
# numbers = [5, 0, 2, 7]

def solution(numbers):
    from itertools import combinations as a
    sumList = list(a(numbers, 2))
    answer = []
    for i in range(len(sumList)):
        answer.append(sumList[i][0] + sumList[i][1])

    return sorted(list(set(answer)))

print(solution(numbers))