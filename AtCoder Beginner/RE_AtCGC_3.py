s = int(input())
s1 = s % 10
s2 = int(s / 10) % 10
s3 = int(s / 100)

sum = s1 + s2 + s3
print(sum)