import sys

# if __name__ == "__main__":
#     meet = []
#     n = int(sys.stdin.readline())
#     for _ in range(n):
#         meet.append(tuple(map(int, sys.stdin.readline().split())))
#     meet.sort(key = lambda x : (x[1],x[0]))

#     end = meet[0][1]
#     cnt = 1

#     for i in range(1,n):
#         if meet[i][0] >= end:
#             end = meet[i][1]
#             cnt += 1
#     print(cnt)


# 다시 풀어봄
n = int(sys.stdin.readline())

room = []
count = 0
check = 0

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    room.append([start, end])
    
room = sorted(room, key = lambda x: (x[1], x[0]))

for time in room:
    if time[0] >= check:
        count += 1
        check = time[1]

print(count)