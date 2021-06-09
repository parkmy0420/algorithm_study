board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    basket = []
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0 :
                if basket == [] or basket[-1] != board[j][moves[i]-1]:
                    basket.append(board[j][moves[i]-1])
                    board[j][moves[i] - 1] = 0
                    break
                else :
                    answer += 2
                    del basket[-1]
                    board[j][moves[i] - 1] = 0
                    break
            else:
                continue
    return answer

print(solution(board,moves))