# arr = [5, 9, 7, 10]
# divisor = 5
arr = [2, 36, 1, 3]
divisor = 1
# arr = [3, 2, 6]
# divisor = 10

def solution(arr, divisor):
    answer = []
    [answer.append(arr[i]) for i in range(len(arr)) if arr[i] % divisor == 0]
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)

print(solution(arr, divisor))