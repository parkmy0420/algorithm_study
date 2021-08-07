n = list(input())
def solution(n):
    most = []
    n_copy = n.copy()
    for i in range(len(n)):
        check = n_copy[i]
        n_copy[i] = '_'
        check_list = n_copy.copy()
        while True:
            if ''.join(check_list).rfind(check) == -1:
                break
            else:
                index = ''.join(check_list).rfind(check)+i
                check_list = n_copy[i:index]
                for j in range(0, len(check_list)//2+1):
                    if check_list[j] == check_list[-j]:
                        if j == len(check_list)//2:
                            if len(most) < len(n[i:index+1]):
                                most = n[i:index+1]
                                check_list = []
                                break
                    else:
                        break
    return ''.join(most) if len(most) != 0 else ''

print(solution(n))