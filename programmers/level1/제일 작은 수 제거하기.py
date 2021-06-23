# arr = [4, 3, 2, 1]
arr = [10]

def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
    else:
        del arr[arr.index(min(arr))]
    return arr

print(solution(arr))