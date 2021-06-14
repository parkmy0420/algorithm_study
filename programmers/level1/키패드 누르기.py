numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"

def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = [3, 0]
    right = [3, 2]
    usehand = ''
    breaker = False

    for i in range(len(numbers)):
        for j in range(4) :
            for k in range(3):
                if keypad[j][k] == numbers[i]:
                    handplace = [j, k]
                    breaker = True
                    break
            if breaker == True:
                breaker = False
                break

        if numbers[i] in (1, 4, 7):
            usehand += 'L'
            left = handplace
        elif numbers[i] in (3, 6, 9):
            usehand += 'R'
            right = handplace
        elif numbers[i] in (2, 5, 8, 0):
            if (abs(handplace[0] - left[0]) + abs(handplace[1] - left[1]) >
            abs(handplace[0] - right[0]) + abs(handplace[1] - right[1])):
                usehand += 'R'
                right = handplace
            elif (abs(handplace[0] - left[0]) + abs(handplace[1] - left[1]) <
            abs(handplace[0] - right[0]) + abs(handplace[1] - right[1])):
                usehand += 'L'
                left = handplace
            else :
                if hand == 'left':
                    usehand += 'L'
                    left = handplace
                elif hand == 'right':
                    usehand += 'R'
                    right = handplace

    return usehand

print(solution(numbers,hand))