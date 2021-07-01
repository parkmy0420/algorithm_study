# arr1, arr2 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
arr1, arr2 = [[1], [2]], [[3], [4]]

def solution(arr1, arr2):
    temp, result = [], []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        result.append(temp)
        temp = []
    return result

print(solution(arr1, arr2))
