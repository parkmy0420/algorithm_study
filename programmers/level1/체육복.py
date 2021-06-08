n = 5
lost = [2,4]
reserve = [3]

def solution(n, lost, reserve):
    students = [1]*n

    #잃어버린 학생
    for i in range(len(lost)):
        students[lost[i]-1] -= 1

    #여분 체육복을 가져온 학생
    for i in range(len(reserve)):
        students[reserve[i] - 1] += 1

    for i in range(len(students)):
        if students[0] == 0 and students[1] == 2: # 맨 첫번째 학생이 체육복을 잃어버린 경우
            students[0] += 1
            students[1] -= 1

        # n번째 학생이 체육복을 잃어버린 경우
        if i == n-1 and students[n-1] == 0 and students[n-2] == 2:
            students[n-1] += 1
            students[n-2] -= 1

        # 1,n번째가 아닌 학생이 체육복을 잃어버린 경우
        if students[i] == 0:
            if i != 0 and students[i-1] == 2:
                students[i] += 1
                students[i-1] -= 1
            elif i != n-1 and students[i+1] == 2:
                students[i] += 1
                students[i+1] -= 1

    return n - students.count(0)

print(solution(n,lost,reserve))