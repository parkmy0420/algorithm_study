w, h = 8, 12

def solution(w,h):
    a = w * h
    sum = w + h
    while(h > 0):
        w, h = h, w % h
    return a - (sum - w)

print(solution(w, h))
