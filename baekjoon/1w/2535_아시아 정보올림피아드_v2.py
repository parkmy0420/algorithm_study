student_num = int(input())
info = [[*map(int, input().split())] for _ in range(student_num)]
info = sorted(info, key=lambda x: (-x[2]))  # 인덱스 2번 기준으로 내림차순
n_check = []    # 국가별 수상자 체크 리스트

for i in range(len(info)):
    if n_check.count(info[i][0]) != 2:
        print(f'{info[i][0]} {info[i][1]}')
        n_check.append(info[i][0])
    if len(n_check) == 3:
        break


