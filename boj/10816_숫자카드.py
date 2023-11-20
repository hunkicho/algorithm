# 해시를 이용하여 숫자갯수 저장

import sys

card = {}
n = int(sys.stdin.readline())


card_list = list( sys.stdin.readline().split())
for i in card_list:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

m = int(sys.stdin.readline())

number_list = list( sys.stdin.readline().split())

for j in number_list:
    if j in card:
        print(card[j])
    else:
        print(0)
