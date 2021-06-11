# d = [1,3,2,5,4]
# budget = 9
d = [2,2,3,3]
budget = 10

def solution(d, budget):
    answer = 0
    for i in range(len(d)):
        if budget >= min(d):
            answer += 1
            budget -= min(d)
            d.remove(min(d))
    return answer

print(solution(d,budget))