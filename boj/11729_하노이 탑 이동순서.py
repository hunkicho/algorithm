import sys

def hanoi(count, start, end):
    global check

    if count > 1:
        hanoi(count-1, start, 6-start-end)
    
    move.append((start, end))
    check += 1
    
    if count > 1:
        hanoi(count-1, 6-start-end, end)
        
count = int(sys.stdin.readline())
check = 0
move = []

hanoi(count, 1, 3)

print(check)
for i in move:
    print(i[0], i[1])
    