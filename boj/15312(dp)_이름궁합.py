import sys

alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
name1 = str(sys.stdin.readline().strip())
name2 = str(sys.stdin.readline().strip())
dp = []

for i in range(len(name1)):
    dp.append(alpha[ord(name1[i]) - 65])
    dp.append(alpha[ord(name2[i]) - 65])

while len(dp) > 2:
    tmp = []
    for i in range(len(dp) - 1):
        tmp.append(int(str(dp[i] + dp[i+1])[-1]))
    dp = tmp


print(str(dp[0]) + str(dp[1]))