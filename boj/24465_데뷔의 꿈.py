import sys
from collections import defaultdict


stars = [0,20, 19, 21, 20, 21, 22, 23, 23, 23, 23, 23, 22]
member = {}

for _ in range(7):
    month, day = map(int, sys.stdin.readline().split())
    birthday_number = month if stars[month] <= day else month - 1 if month > 1 else 12 

    if birthday_number in member:
        member[birthday_number] += 1
    else:
        member[birthday_number] = 1

apply_count = int(sys.stdin.readline())
pass_people = defaultdict(list)

for _ in range(apply_count):
    month, day = map(int, sys.stdin.readline().split())
    birthday_number = month if stars[month] <= day else month - 1 if month > 1 else 12

    if not birthday_number in member:
        pass_people[month].append(day)

length = len(pass_people)

if (length > 0):
    sorted_dict = sorted(pass_people.items())
    for item in sorted_dict:
        item[1].sort()
        for day in item[1]:
            print(f"{item[0]} {day}")
else:
    print("ALL FAILED")
