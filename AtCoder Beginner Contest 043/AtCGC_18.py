n = int(input())
array = list(map(int, input().split()))
ave = sum(array) / len(array)
ave2 = round(ave)
cost = 0
for i in array:
    cost += (i-ave2) * (i-ave2)
print(cost)