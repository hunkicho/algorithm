# def solution(people, limit):
#     answer = 0
#     #people.sort()
#     stack = []
#     i = 0
    
#     while True:
#         if len(people) < 1:
#             break
#         check = people[i]
#         if limit - check in people:
#             try:
#                 people.remove(check)
#                 people.remove(limit - check)
#             except:
#                 answer += 1
#                 break
#         else:
#             people.remove(check)

#         answer += 1
   
#     return answer

def solution(people, limit):
    people.sort()
    count = 0

    first = 0
    last = len(people) - 1
    while first < last:
        if people[first] + people[last] <= limit:
            first += 1

        last -= 1

        count += 1

    if first == last:
        count += 1

    return count