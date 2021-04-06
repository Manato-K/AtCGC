a = 1234567890
sum = 0

for i in range(2000000):
    if i != 0:
        if a % i == 0:
            sum += i

print("{0}".format(sum))