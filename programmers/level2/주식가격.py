prices = [1, 2, 3, 2, 1, 2, 3]

def solution(prices):
    answer = [n for n in range(len(prices)-1, -1, -1)]
    stack = [0]
    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    return answer

print(solution(prices))