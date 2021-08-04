rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# rows, columns, queries = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# rows, columns, queries = 100, 97, [[1,1,100,97]]


def solution(rows, columns, queries):
    matrix = [[(i*columns+j+1) for j in range(columns)] for i in range(rows)]
    answer = []
    for k in range(len(queries)):
        start0, start1, end0, end1 = queries[k][0]-1, queries[k][1]-1, queries[k][2]-1, queries[k][3]-1
        now = [start0, start1]
        temp = [matrix[now[0]][now[1]]]
        cnt = 0

        while True:
            if start0 == now[0] and end1 != now[1]:
                temp.append(matrix[now[0]][now[1] + 1])
                matrix[now[0]][now[1] + 1] = temp[cnt]
                now[1] += 1
            elif end1 == now[1] and end0 != now[0]:
                temp.append(matrix[now[0] + 1][now[1]])
                matrix[now[0] + 1][now[1]] = temp[cnt]
                now[0] += 1
            elif end0 == now[0] and start1 != now[1]:
                temp.append(matrix[now[0]][now[1] - 1])
                matrix[now[0]][now[1] - 1] = temp[cnt]
                now[1] -= 1
            else:
                temp.append(matrix[now[0] - 1][now[1]])
                matrix[now[0] - 1][now[1]] = temp[cnt]
                now[0] -= 1
            cnt += 1

            if now == [start0, start1]:
                answer.append(min(temp))
                break

    return answer

print(solution(rows, columns, queries))