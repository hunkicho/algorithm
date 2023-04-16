# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 못풀어서 답 봄

# 내가 한거

# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=int)
    
#     for i in phone_book:
#         for j in phone_book:
#             if i != j and i == j[:len(i)]:
#                 return False
    
#     return answer

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer