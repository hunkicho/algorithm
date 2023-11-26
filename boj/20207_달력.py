import sys

n = int(sys.stdin.readline())
schedule = []
calendar = [[0] * 366 for _ in range(n+1)]

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    schedule.append((start, end, end-start))

schedule = sorted(schedule, key=lambda x : (x[0], -x[2]))

h = 1
s = 365
e = 0
result = 0

for item in schedule:
    temp_y = 1
    for i in range(1, h+1):
        if calendar[i][item[0]] == 0:
            break
        else:
            temp_y += 1
    
    if temp_y == 1 and e != 0:
        temp_check = False
        for j in range(1, h+1):
            if calendar[j][item[0]-1] == 1:
                temp_check = True
                break
        if not temp_check:
            result += (((e -  s)+1) * h)
            h = 1
            s = 365
            e = 0
        
    for i in range(item[0], item[1] + 1):
        calendar[temp_y][i] = 1

    if temp_y > h:
        h = temp_y
    if item[0] < s:
        s = item[0]
    if item[1] > e:
        e = item[1]

result += (((e -  s)+1) * h)
print(result)