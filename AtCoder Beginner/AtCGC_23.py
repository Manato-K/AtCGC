sum = 0
for i in range(30001):
    if int(i % 3) == 0 or '3' in str(i):
        sum += i
print(sum)
