import sys

if __name__ == "__main__":
    while True:
        N = int(sys.stdin.readline())
        result = 0

        if N == -1:
            break

        
        for i in range(N, 1, -1):
            coconut = N

            for _ in range(i):
                coconut -= 1
                if coconut % i > 0:
                    break
                divide = coconut // i
                coconut -= divide

            if coconut % i == 0:
                result =  i
                break

        if result == 0:
            print(f"{N} coconuts, no solution")
        else:
            print(f"{N} coconuts, {result} people and 1 monkey")
