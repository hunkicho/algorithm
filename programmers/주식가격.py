def solution(prices):
    length = len(prices)
    answer = [0] * length
    
    for i in range(length-1):
        second = 1
        for j in range(i+1,length):
            answer[i] = second
            if prices[i] > prices[j]:
                break
            second += 1
    
    return answer


# 책에 나온 답
def solution2(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]: # 스택이 비어있지 않고 맨 위의 원소가 현재 가격보다 크면 
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)
        
    for i in stack:
        answer[i] = len(prices) - 1 - i
        
    return answer

print(solution2([1, 2, 3, 2, 3]))