import sys

# 아래와 같이 입력
# 10 (합계)
# 2 5 3 6 (동전 배열)

if __name__ == "__main__":
    sum = int(sys.stdin.readline()) # 합계
    coins = list(map(int, sys.stdin.readline().split())) # 동전
    coins_len = len(coins)
    dp = [0] * (sum+1)

    # 첫번째 코인 적용
    for q in range(sum+1):
        if q % coins[0] == 0: # 배수일 경우 경우의 수 1개 추가
            dp[q] += 1
    
    # 두번째 코인부터 끝까지
    for i in range(1, coins_len):
        for j in range(coins[i], sum+1):
            dp[j] += dp[j-coins[i]]
    
    print(dp[sum])

