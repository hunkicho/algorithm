import sys
from queue import PriorityQueue

if __name__ == "__main__":
    t, w = map(int, sys.stdin.readline().split())
    time = [0 for _ in range(t+1)]
    tree = [0]
    cnt = 0
    check = 1
    check2 = 0
    tmp2 = 1
    q1 = PriorityQueue()
    q2 = PriorityQueue()
    test = 2

    for i in range(t):
        tmp = int(sys.stdin.readline())
        if tmp == check:
            cnt += 1
        else:
            check2 = tmp
            check = i+1
            break
    print("11111111")
    
    for j in range(t-check):
        tmp = int(sys.stdin.readline())
        if tmp == check2:
            tmp2 += 1
        else:
            check2 = tmp
            if tmp == 1:
                q1.put(-tmp2)
            else:
                q2.put(-tmp2)
            tmp2 = 1
    print("22222222")
    print(q1)
    print(q2)
    for k in range(w):
        if test == 2:
            v = q2.get()
            print(v,"2")
            cnt += -v
            test = 1
        else:
            v = q1.get()
            print(v,"1")
            cnt += -v
            test = 2
    print(cnt)


    
    