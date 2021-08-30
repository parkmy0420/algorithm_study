# word = "AAAAE"
# word = "AAAE"
# word = "I"
word = "EIO"

from itertools import product
def solution(word):
    wordlist = ['A','E','I','O','U']    # 문자 종류
    productlist = ['A','E','I','O','U'] # 사전
    for i in range(2,6):
        # 데카르트 곱 (2부터 문자의 종류 개수만큼), 튜플 -> list형태로
        temp = list(map(list, product(wordlist, repeat=i)))
        for j in range (len(temp)): # 이차원 리스트를 str 일차원 리스트로 변환
            productlist.append(''.join(temp[j]))
    productlist.sort()  # 사전 순 정렬
    return productlist.index(word)+1    # 인덱스는 0번 부터라 +1 해주기

print(solution(word))