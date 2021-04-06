n = int(input())
a = []
sum = []

for i in range(n):
    a.append(int(input()))
a.sort()
cnt = n
for i in a:
    for height in sum:
        if i == height:
            cnt -= 1
            break
    else:
        sum.append(i)
print(cnt)