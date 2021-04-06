# 205円切手が30枚、82円切手が40枚、30円切手が10枚あります。
# これらの切手の全部または一部（1枚以上）を使って額面の和として表せる金額は何通りあるか、
# 求めてください。
a = int(input())
b = int(input())
c = int(input())
cnt = 0
sum = 0
x = [0]*12000
for a in range(a+1):
    for b in range(b + 1):
        for c in range(c + 1):
            sum = 205 * a + 82 * b + 30 * c
            if x[sum] == 0:
                x[sum] = 1
                cnt += 1
print(cnt)