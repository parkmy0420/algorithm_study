# numbers, target = [1, 1, 1, 1, 1], 3
numbers, target = [1, 2, 3, 4, 5], 5


def solution(numbers, target):
    from itertools import combinations
    sumlist = sum(numbers)
    a = []

    if (sumlist - target) % 2 == 0: # 리스트의 합에서 target을 뺏을때 2로 나누어지는가
        minus = int((sumlist - target) / 2)
        for i in range(1, len(numbers)+1):
            a = a + list(combinations(numbers, i))

        for j in range(len(a)):
            a[j] = sum(a[j])
        return a.count(minus)

    # 2로 나누어지지 않는다면 리스트로 target을 만들 수 없다.
    else: return 0

print(solution(numbers, target))