import sys

n = int(sys.stdin.readline())
water = list(map(int, sys.stdin.readline().split()))
water.sort()

result = 2000000000
final_result = []
lp = 0 
rp = n - 1

fl = 0
fr = 0

while lp < rp:
    hap = water[lp] + water[rp]

    if abs(hap) < abs(result):
        result = hap
        fl = lp
        fr = rp

    if hap > 0:
        rp -= 1
    else:
        lp += 1

print(water[fl], water[fr])