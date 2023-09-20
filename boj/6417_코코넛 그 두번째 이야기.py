import sys

if __name__ == "__main__":
    while True:
        N = int(sys.stdin.readline())
        result = 0

        if N == -1:
            break

        
        for i in range(N, 1, -1):
            print(i)
            after_monkey = N

            for _ in range(i):
                after_monkey -= 1
                if after_monkey % i > 0:
                    break
                divide = after_monkey // i
                after_monkey -= divide

            if after_monkey % i == 0:
                result =  i
                break
        if result == 0:
            print(N,"coconuts, no solution")
        else:
            print(N,"coconuts,",result,"people and 1 monkey")
