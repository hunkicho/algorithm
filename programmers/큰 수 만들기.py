from itertools import combinations

def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    print(st)
    return ''.join(st[:len(st) - k])


print(solution("1924",2))
