record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    a, answer = [], []
    for i in range(len(record)):
        a += [record[i].split(sep=' ')]
    user = {}
    for i in range(len(a)):
        if a[i][0] == 'Change':
            user[a[i][1]] = a[i][2]
        elif a[i][0] == 'Enter':
            user[a[i][1]] = a[i][2]
        else:
            continue

    for i in range(len(a)):
        if a[i][0] == 'Enter':
            answer.append(f'{user[a[i][1]]}님이 들어왔습니다.')
        elif a[i][0] == 'Leave':
            answer.append(f'{user[a[i][1]]}님이 나갔습니다.')
        else:
            continue

    return answer

print(solution(record))