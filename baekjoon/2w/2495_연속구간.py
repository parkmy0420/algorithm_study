for i in [input() for _ in range(3)]:
    length, check = 1, 1
    for j in range(7):
        if i[j] == i[j+1]:
            check += 1
            if length < check:
                length = check
        else:
            check = 1
    print(length)
