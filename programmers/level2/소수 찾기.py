# numbers = '17'
numbers = '011'

def solution(numbers):
    from itertools import permutations
    numbers = list(numbers)
    numlist, cnt = [], 0
    for i in range(1, len(numbers)+1):
        numlist += list(permutations(numbers,i))
    for j in range(len(numlist)):
        numlist[j] = int(''.join(list(numlist[j])))
    numlist = sorted(list(set(numlist)))

    # 소수 구하기
    arr = []
    for l in range (numlist[-1]+1):
        arr.append(l)

    for k in range(2, len(arr)):
        for m in range(2*k, len(arr), k):
            arr[m] = False

    arr = list(set(arr))
    arr.remove(arr.index(1))
    arr.remove(arr.index(0))

    for n in numlist:
        if n in arr:
            cnt += 1

    return cnt

print(solution(numbers))