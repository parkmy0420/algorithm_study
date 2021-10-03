readlist = [input() for _ in range(5)]

for i in range(len(max(readlist, key=len))):    # 문자열 중 가장 긴 길이만큼 for문
    for j in range(5):  # 문자열 개수
        if len(readlist[j]) > i:   # 해당 문자열이 다 출력되지 않았으면 다음 실행
            print(readlist[j][i], end='')
#

# readlist = [input() for _ in range(5)]
# max = len(max(readlist, key=len))
# for j in range(5):
#     if len(readlist[j]) != max:
#         for k in range(max - len(readlist[j])):
#             readlist[j] += ' '
#
# print(''.join(sum(list(map(list, zip(*readlist))), [])).replace(' ',''))
