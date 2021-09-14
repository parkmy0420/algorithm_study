# enter, leave = [1,3,2], [1,2,3]
enter, leave = [1,4,2,3], [2,1,3,4]
# enter, leave = [3,2,1], [2,1,3]
# enter, leave = [3,2,1], [1,3,2]
# enter, leave = [1,4,2,3], [2,1,4,3]

def solution(enter, leave):
    answer = [0]*len(enter)
    room = []
    for i in range(len(enter)):
        room.append(enter.pop(0))
        while len(leave) != 0 and leave[0] in room:
            answer[room.pop(room.index(leave[0]))-1] += len(room)
            del leave[0]
            for j in room:
                answer[j-1] += 1
    return answer

print(solution(enter, leave))