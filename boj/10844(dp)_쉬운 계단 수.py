n = int(input())
dy = [0] * (n + 1)
dy[1] = 9
dy[2] = 17

for i in range(3, n+1):
    dy[i] = (dy[i-1] * 2) - 2
print(dy[n] % 1000000000)