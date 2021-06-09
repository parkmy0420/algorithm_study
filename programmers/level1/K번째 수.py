array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        sliceArray = array[commands[i][0]-1:commands[i][1]]
        sliceArray.sort()
        answer.append(sliceArray[commands[i][2]-1])
    return answer

print(solution(array,commands))